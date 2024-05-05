from PIL import Image, ImageOps
import sys
import os


if (os.path.splitext(sys.argv[1]))[1] != (os.path.splitext(sys.argv[2]))[1]:
    sys.exit("w")


with Image.open(sys.argv[1]) as file1, Image.open("shirt.png") as file3:
    size = file3.size
    file1 = ImageOps.fit(file1,size)
    file1.paste(file3,file3)

    file1.save(sys.argv[2])
