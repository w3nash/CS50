from random import choice
from english_words import get_english_words_set
from printer import newline, inline, Colors
import os


dictionary = get_english_words_set(["web2"], lower=True)
error = ""

class Wordblock:
    def __init__(self):
        self._scores = []
        self._blocks = []
        for _ in range(6):
            inner_list = []
            for _ in range(5):
                inner_list.append(Colors.WHITE_BG + " _ " + Colors.RESET_ALL)
            self._blocks.append(inner_list)
        for _ in range(6):
            inner_list = []
            for _ in range(5):
                inner_list.append(0)
            self._scores.append(inner_list)

    def print_wordblock(self):
        print()
        for chars in self._blocks:
            for word in chars:
                print(word, end="")
            print()

    def add_word(self, guess, attempts):
        """ Add the word in the word block. """
        for i in range(5):
            if self._scores[attempts][i] == 2:
                self._blocks[attempts][i] = Colors.GREEN_BG + " " + guess[i].upper() + " " + Colors.RESET_ALL
            elif self._scores[attempts][i] == 1:
                self._blocks[attempts][i] = Colors.YELLOW_BG+ " " + guess[i].upper() + " " + Colors.RESET_ALL
            else:
                self._blocks[attempts][i] = Colors.RED_BG + " " + guess[i].upper() + " " + Colors.RESET_ALL


    def check_words(self, guess, toguess, attempts):
        """ Compare two strings (guess, toguess) """
        for i in range(5):
            for j in range(5):
                if guess[i] == toguess[j]:
                    if i == j:
                        self._scores[attempts][i] = 2
                        break
                    else:
                        self._scores[attempts][i] = 1
        self.add_word(guess, attempts)
        if guess == toguess:
            return True
        return False


def main():
    while True:
        global error
        print_menu(0)
        try:
            option = int(input(Colors.BLUE + "\n📝 Select: " + Colors.RESET_ALL))
        except ValueError:
            error = "⚠️ Please enter valid choice."
            continue
        except (KeyboardInterrupt, EOFError):
            newline(Colors.RED, "\n🕹️ You have exited the game. Thank you for playing. 👌")
            break

        match option:
            case 1:
                to_guess = get_word()
                block = Wordblock()
                attempts = 0
                while True:
                    print_menu(option)
                    newline(Colors.BLUE, "ℹ️ The word starts with the letter " + to_guess[0].upper())
                    block.print_wordblock()
                    newline(Colors.YELLOW, "\nYou have " + str(6 - attempts) + " attempts remaning.")
                    player_guess = get_guess()
                    result = block.check_words(player_guess, to_guess, attempts)
                    if result:
                        print_result(result, to_guess, attempts, block.print_wordblock)
                        break
                    elif attempts == 5:
                        print_result(result, to_guess, attempts, block.print_wordblock)
                        break
                    else:
                        attempts += 1

            case 2:
                print_menu(option)
                word = input(Colors.BLUE + "\n📝 Enter a word to add: " + Colors.RESET_ALL).strip().lower()
                if not add_word(word):
                    error = "⚠️ Please enter valid english word."
                else:
                    error = ""

            case 3:
                print_menu(option)
                input(Colors.BLUE + "\n📝 Press enter to continue..." + Colors.RESET_ALL)
                error = ""

            case 4:
                newline(Colors.RED, "\n🕹️ You have exited the game. Thank you for playing. 👌")
                break

            case _:
                error = "⚠️ Please enter valid choice."


def clear():
    """ Clear the terminal """
    os.system("cls" if os.name == "nt" else "clear")


def get_guess():
    """Get a guess from user and validate"""
    global dictionary
    while True:
        guess = input(Colors.BLUE +"🤔 Enter your guess 📝: " + Colors.RESET_ALL).strip().lower()
        if len(guess) != 5:
            newline(Colors.YELLOW, "⚠️ You are supposed to enter a 5 letter word.")
            continue
        if guess not in dictionary:
            newline(Colors.YELLOW, "⚠️ Not a valid english word. Should not be in a form of plural.")
            continue
        return guess


def get_word():
    """Get a word from words.txt"""
    try:
        with open("words.txt") as file:
            words = []
            for line in file:
                words.append(line.strip())
            return choice(words)
    except FileNotFoundError:
        raise FileNotFoundError("Did you have a filed called words.txt?")


def add_word(towrite):
    """Add a word to words.txt"""
    global dictionary
    if len(towrite) != 5:
        return False
    with open("words.txt", "a") as file:
        if towrite in dictionary:
            file.write(towrite + "\n")
            newline(Colors.GREEN, "\n🕹️ You have added the word, " + towrite.upper())
            input(Colors.BLUE + "\n📝 Press enter to continue..." + Colors.RESET_ALL)
            return True
        return False


def print_result(iswinner, toguess, attempts, block):
    """ Print result in the end. """
    print_menu(3)
    block()
    if iswinner:
        newline(Colors.CYAN, "🎊 CONGRATULATIONS! 🎉")
        newline(Colors.CYAN, "🥳 YOU ARE CORRECT AND YOU WON! 🙌")
        newline(Colors.CYAN, "🤔 WORD TO GUESS 📝: " + Colors.WHITE + toguess);
        newline(Colors.CYAN, "🔎 NO. OF ATTEMPTS 👌: " + Colors.WHITE + str(attempts + 1))
    else:
        newline(Colors.CYAN, "😔 VERY SAD! 💔")
        newline(Colors.CYAN, "🥲 YOU ARE OUT OF ATTEMPTS AND YOU LOSE. 0️⃣")
        newline(Colors.CYAN, "🤔 WORD TO GUESS 📝: " + Colors.WHITE + toguess)
    input(Colors.BLUE + "\n📝 Press enter to continue..." + Colors.RESET_ALL)


def print_menu(num):
    global error
    clear()
    print(Colors.CYAN)
    print("                                 ,------.  ")
    print(",--.  ,--.,--.   ,--.,--.   ,--.'  .--.  ' ")
    print("|  '--'  ||   `.'   ||   `.'   |'--' _|  | ")
    print("|  .--.  ||  |'.'|  ||  |'.'|  | .--' __'  ")
    print("|  |  |  ||  |   |  ||  |   |  | `---'     ")
    print("`--'  `--'`--'   `--'`--'   `--' .---.     ")
    print("                                 '---'     ")
    newline(Colors.CYAN, "🤔 Hmm? - A Word Guesser Game 🕹️")
    newline(Colors.GREEN, "😎 By: Jonash Marcelino 👌")
    newline(Colors.PURPLE, "💻 Github: w3nash 🤖")
    print(Colors.RESET_ALL)

    if error:
        newline(Colors.RED, error)

    match num:
        case 0:
            newline(Colors.CYAN, "🤔 MAIN MENU 📝")
            newline(Colors.CYAN, "1. 🕹️ PLAY")
            newline(Colors.CYAN, "2. 📕 ADD A WORD")
            newline(Colors.CYAN, "3. 💻 CREDITS")
            newline(Colors.CYAN, "4. ❎ EXIT")

        case 1:
            newline(Colors.CYAN, "🤔 PLAYING HMM? - A WORD GUESSER GAME 🕹️")
            newline(Colors.CYAN, "ℹ️ The game have already randomly selected a 5 letter word. 📖")
            newline(Colors.CYAN, "ℹ️ Now, try guessing and I will help you in this challenge. 🔍")
            newline(Colors.CYAN, "ℹ️ I will change the background color of the text as a hint! 🪄")
            inline(Colors.CYAN, "ℹ️ " + Colors.RED_BG + " X ")
            newline(Colors.CYAN, " means wrong letter.")
            inline(Colors.CYAN, "ℹ️ " + Colors.YELLOW_BG + " X ")
            newline(Colors.CYAN, " means correct letter but at wrong position.")
            inline(Colors.CYAN, "ℹ️ " + Colors.GREEN_BG + " X ")
            newline(Colors.CYAN, " means correct letter and correct position.")

        case 2:
            newline(Colors.CYAN, "🤔 ADD A WORD 📕")
            newline(Colors.BLUE, "ℹ️ Here you can add a new word so that you can put it onto practice. 📖")

        case 3:
            newline(Colors.BLUE, "💻 CREDITS")
            newline(Colors.PURPLE, "🧑‍💻 Developer:")
            newline(Colors.CYAN, "Jonash Marcelino\n")
            newline(Colors.PURPLE, "🤖 ChatGPT Gang: (Support)")
            newline(Colors.CYAN, "Anthony James Bargo")
            newline(Colors.CYAN, "John Gabriel Cuadro")
            newline(Colors.CYAN, "Vaughn Tinte")
            newline(Colors.CYAN, "Takeshi Okamoto")
            newline(Colors.CYAN, "Jhorel Jerard Franco")


if __name__ == "__main__":
    main()
