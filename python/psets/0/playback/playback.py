def main():
    inp = input().strip()
    print(playback(inp))


def playback(to):
    return to.replace(" ", "...")


if __name__ == "__main__":
    main()
