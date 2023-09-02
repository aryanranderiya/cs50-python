import sys
from PIL import Image,ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

file1name,file1extension = sys.argv[1].split(".")
file2name,file2extension = sys.argv[2].split(".")

extensiontypes = ["png","jpg","jpeg",]

if file2extension not in extensiontypes :
    sys.exit("Invalid output")

if file1extension != file2extension :
    sys.exit("Input and output have different extensions")

with Image.open("shirt.png") as shirt, Image.open(sys.argv[1]) as muppet :
    muppet = ImageOps.fit(muppet, shirt.size)
    muppet.paste(shirt,shirt)
    muppet.save(sys.argv[2])

