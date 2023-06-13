def main():
    inp = input().strip()
    print(faces(inp))


def faces(to):
    return to.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()
