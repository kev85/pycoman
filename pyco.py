#!/usr/bin/python3
from pathlib import Path
import pathlib
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import random

#initialise dictionary with images from folder
#TODO: create secondary dict for used images (used later)
imgPaths = []
for imgpath in pathlib.Path('images').iterdir():
    if imgpath.suffix == '.jpg':
        imgPaths.append(imgpath)

#find image to put into replace function as long as it hasn't already been used
def putImg():
    img = random.choice(imgPaths)
    for img in imgPaths:
        img = random.choice(imgPaths)
        str_img = img
        path = Path(str_img)
        replace("index.html", "image2.jpg", "str_img")

#function to replace string in HTML file - ensure HTML file is REALLY SMALL as this will read every line in it & could otherwise be a memory hog
def replace(file_path, pattern, subst):
    fh, the_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    remove(file_path)
    move(the_path, file_path)

#cal function to do image insert/dictionary collection
putImg()