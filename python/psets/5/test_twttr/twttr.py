def main():
    text = input("Input: ").strip()
    print("Output:", shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    output = ""
    for c in word.strip():
        if c.lower() not in vowels:
            output += c
    return output


if __name__ == "__main__":
    main()
