import sys
from PIL import Image, ImageOps


def main():
    extentions = (".jpg", ".jpeg", ".png")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(extentions):
        sys.exit("Invalid input")
    if not sys.argv[2].endswith(extentions):
        sys.exit("Invalid output")
    if (
        sys.argv[1][sys.argv[1].rfind(".") + 1 :]
        != sys.argv[2][sys.argv[2].rfind(".") + 1 :]
    ):
        sys.exit("Input and output have different extensioyesns")

    try:
        with Image.open(sys.argv[1]) as input_img:
            with Image.open("shirt.png") as shirt_img:
                input_img = ImageOps.fit(input_img, shirt_img.size)
                input_img.paste(shirt_img, mask=shirt_img)
                input_img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
