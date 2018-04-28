import numpy as np
import matplotlib.pyplot as plt
import colorsys
from PIL import Image
import json
import os, sys
import colorsys

def readImgPixels(filename):
    # (1) Import the file to be analyzed!
    img_file = Image.open(filename)
    img = img_file.load()

    # (2) Get image width & height in pixels
    [xs, ys] = img_file.size
    xStep = 97;
    yStep = 50;
    # create a list for different values
    colorList=[]
    # Examine each pixel in the image file 
    for x in range(0, xs, xStep):
      for y in range(0, ys, yStep):
        # (4)  Get the RGB color of the pixel
        print(x,y)
        colorList.append(getAverageColor(x,y,xStep,yStep,img))
    colorList.sort(key=get_hsv)
    return colorList

def getAverageColor(x, y, xStep, yStep, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x, x+xStep):
        for t in range(y, y+yStep):
            pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    hexrgb = ("#"+format(r//count,'02x')+format(g//count,'02x')+format(b//count,'02x'))
    return hexrgb


def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

def main():
    fileList = os.listdir("time")
    obj_list=list(range(1923, 2019))
    counter = 0
    for yr in range(1923, 2019):
        filename = os.path.join("time", "Time-"+str(yr)+".jpg")
        obj_list[counter] = {}
        obj_list[counter]["year"]= yr
        obj_list[counter]["colorList"]=readImgPixels(filename)
        counter += 1
    with open("data.json", "w") as f:
        json.dump(obj_list, f, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': '))


main()