class Colors:
    # Reset
    RESET_ALL = "\u001B[0m"

    # Text colors
    BLACK = "\u001B[30m"
    RED = "\u001B[31m"
    GREEN = "\u001B[32m"
    YELLOW = "\u001B[33m"
    BLUE = "\u001B[34m"
    PURPLE = "\u001B[35m"
    CYAN = "\u001B[36m"
    WHITE = "\u001B[37m"

    # Background colors
    BLACK_BG = "\u001B[40m"
    RED_BG = "\u001B[41m"
    GREEN_BG = "\u001B[42m"
    YELLOW_BG = "\u001B[43m"
    BLUE_BG = "\u001B[44m"
    URPLE_BG = "\u001B[45m"
    CYAN_BG = "\u001B[46m"
    WHITE_BG = "\u001B[47m"


def inline(color, text):
    print(color + text + "\u001B[0m", end="")


def newline(color, text):
    print(color + text + "\u001B[0m")
