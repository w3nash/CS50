def main():
    text = input("Input: ").strip()
    vowels = ["a", "e", "i", "o", "u"]
    output = ""
    for c in text:
        if c.lower() not in vowels:
            output += c
    print("Output:", output)


if __name__ == "__main__":
    main()
