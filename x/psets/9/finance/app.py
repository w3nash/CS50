import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute(
        'SELECT symbol, sname, SUM(shares) as shares, price FROM transactions WHERE user_id = ? GROUP BY symbol', session["user_id"])
    cash = db.execute('SELECT cash FROM users WHERE id = ?', session["user_id"])
    totals = {}
    prices = {}
    for stocks in rows:
        stock = lookup(stocks["symbol"])
        prices[stocks["symbol"]] = stock["price"]
        totals[stocks["symbol"]] = (float(stocks["shares"]) * float(stock["price"]))
    total = cash[0]["cash"] + sum(totals.values())
    return render_template("index.html", stocks=rows, cash=cash[0]["cash"], total=total, prices=prices, totals=totals)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Symbol is required.")
        elif not shares:
            return apology("Shares is required.")
        elif not shares.isnumeric() or int(shares) < 1:
            return apology("Shares is not valid.")

        info = lookup(symbol)
        if info == None:
            return apology("Symbol is not valid.")

        rows = db.execute('SELECT cash FROM users WHERE id = ?', session["user_id"])
        cash = rows[0]["cash"]

        total = float(info["price"]) * float(shares)
        if float(total) > float(cash):
            return apology("Not enough cash.")

        now = datetime.datetime.utcnow()

        db.execute('INSERT INTO transactions (symbol, sname, shares, price, method, transacted, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   info["symbol"], info["name"], shares, info["price"], "BUY", now.strftime('%Y-%m-%d %H:%M:%S'), session["user_id"])

        db.execute('UPDATE users SET cash = ? WHERE id = ?', cash - total, session["user_id"])

        return redirect("/")
    else:
        symbols = db.execute('SELECT DISTINCT(symbol) FROM transactions WHERE user_id = ?', session["user_id"])
        return render_template("buy.html", symbols=symbols)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute(
        'SELECT symbol, sname AS name, shares, price, method, transacted FROM transactions WHERE user_id = ?', session["user_id"])
    if len(rows) == 0:
        rows = None
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Symbol is required.")

        info = lookup(symbol)
        if info == None:
            return apology("Symbol is invalid.")
        return render_template("quoted.html", info=info)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirmation")

        if not username:
            return apology("Username is required.")
        elif not password:
            return apology("Password is required.")
        elif not password:
            return apology("Password minimum length is 8.")
        elif not confirm:
            return apology("You need to confirm your password.")
        elif password != confirm:
            return apology("Does not match.")

        usenames = db.execute('SELECT * FROM users WHERE username = ?', username)
        if (len(usenames) != 0):
            return apology("Username already taken.")

        hashed = generate_password_hash(password)
        db.execute('INSERT INTO users (username, hash) VALUES (?, ?)', username, hashed)

        rows = db.execute('SELECT id FROM users WHERE username = ?', username)
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        rows = db.execute('SELECT DISTINCT(symbol), shares FROM transactions WHERE user_id = ?', session["user_id"])

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        symbolList = []
        for row in rows:
            symbolList.append(row["symbol"])

        if not symbol:
            return apology("Symbol is required.")
        elif not shares:
            return apology("Shares is required.")
        elif symbol not in symbolList:
            return apology("You don't have this shares.")

        share = db.execute('SELECT shares FROM transactions WHERE user_id = ? AND symbol = ?', session["user_id"], symbol)
        if len(share) == 0:
            return apology("You don't have this shares.")

        totalShare = share[0]["shares"]
        if int(shares) > int(totalShare):
            return apology("You don't have enought shares.")

        info = lookup(symbol)
        cash = db.execute('SELECT cash FROM users WHERE id = ?', session["user_id"])[0]["cash"]
        total = float(shares) * float(info["price"])

        now = datetime.datetime.utcnow()

        db.execute('INSERT INTO transactions (symbol, sname, shares, price, method, transacted, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   info["symbol"], info["name"], (int(shares) * -1), info["price"], "SELL", now.strftime('%Y-%m-%d %H:%M:%S'), session["user_id"])

        db.execute('UPDATE users SET cash = ? WHERE id = ?', cash + total, session["user_id"])

        return redirect("/")
    else:
        rows = db.execute('SELECT DISTINCT(symbol) FROM transactions WHERE user_id = ?', session["user_id"])
        return render_template("sell.html", rows=rows, )
