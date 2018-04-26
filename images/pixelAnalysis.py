import numpy as np
import matplotlib.pyplot as plt
import colorsys
from PIL import Image
import csv

def readImgPixels(filename, csv):
    # (1) Import the file to be analyzed!
    img_file = Image.open(filename)
    img = img_file.load()

    # (2) Get image width & height in pixels
    [xs, ys] = img_file.size

    # create a list for different values
    colorList=[]
    colorList.append(filename)
    # Examine each pixel in the image file
    for x in xrange(0, xs):
      for y in xrange(0, ys):
        # (4)  Get the RGB color of the pixel
        [r, g, b] = img[x, y]
        colorList.append("#"+format(r,'02x')+format(g,'02x')+format(b,'02x'))

    return colorList


def writeCSV(img):
    with open(<path to output_csv>, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def main():
    fileList=os. time
    for img in imgs

