from random import randint


def main():
    level = get_positive_int("Level: ")
    toguess = randint(1, level)
    while True:
        guess = get_positive_int("Guess: ")
        if guess > toguess:
            print("Too large!")
        elif guess < toguess:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_positive_int(prompt):
    while True:
        try:
            toreturn = int(input(prompt))
            if toreturn > 0:
                return toreturn
        except ValueError:
            pass


if __name__ == "__main__":
    main()
