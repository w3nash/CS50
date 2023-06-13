# TODO
from cs50 import get_string


def main():
    """ Main Function """
    # Get input from user
    text = get_string("Text: ")

    # Counters
    letters = count_letters(text)
    words = len(text.split())
    sentences = count_sentences(text)

    # Calculate the index
    ltr = letters / words * 100
    snt = sentences / words * 100
    index = int(round(0.0588 * ltr - 0.296 * snt - 15.8))

    # Print Grade
    if index < 1:
        print("Before Grade 1")
    elif index >= 17:
        print("Grade 16+")
    else:
        print(f"Grade", index)


def count_letters(txt):
    """ Function that counts letter in text """
    letter_ctr = 0
    for c in txt:
        if c.isalpha():
            letter_ctr += 1
    return letter_ctr


def count_sentences(txt):
    """ Function that counts sentences in text """
    sentence_ctr = 0
    for c in txt:
        if c in ['.', '!', '?']:
            sentence_ctr += 1
    return sentence_ctr


if __name__ == '__main__':
    main()