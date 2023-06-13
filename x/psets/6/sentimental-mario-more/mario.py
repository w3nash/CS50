# TODO
# import get int
from cs50 import get_int

# get input
while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break

# Loop
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    print("#" * (i) + "  " + "#" * (i))
