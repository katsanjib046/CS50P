import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-4:] != '.jpg' and sys.argv[1][-5:] != '.jpeg' and sys.argv[1][-4:] != '.png':
        sys.exit("Invalid input")
    if sys.argv[2][-4:] != '.jpg' and sys.argv[2][-5:] != '.jpeg' and sys.argv[2][-4:] != '.png':
        sys.exit("Invalid output")
    if sys.argv[1].split('.')[1] != sys.argv[2].split('.')[1]:
        sys.exit("Input and output have different extensions")
    shirt = Image.open('shirt.png', 'r')          # main shirt file
    try:
        dummy = Image.open(sys.argv[1], 'r')
        manager(shirt, dummy)
        dummy.close()
    except FileNotFoundError:
        sys.exit("File Not Found!")
    shirt.close()


def manager(shirt, dummy):
    """Takes the shirt and a dummy to make the necessary image"""
    shirt_size = shirt.size
    dummy = ImageOps.fit(dummy, shirt_size)
    dummy.paste(shirt, shirt)
    dummy.save(sys.argv[2])

############ Testing #############
if __name__ == "__main__":
    main()