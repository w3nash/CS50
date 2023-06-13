import random


def main():
    level = get_level()
    score, n = 0, 10

    for _ in range(n):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        for i in range(4):
            if i == 3:
                print(f"{x} + {y} = {z}")
                break

            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            else:
                if guess == z:
                    score += 1
                    break
                else:
                    print("EEE")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            toreturn = int(input("Level: "))
            if toreturn > 0 and toreturn <= 3:
                return toreturn
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        min = 0
        max = 9
    else:
        min = 10 ** (level - 1)
        max = (10**level) - 1
    return random.randint(min, max)


if __name__ == "__main__":
    main()
