# import the necessary packages
from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils
import sys
import os
import img2pdf

my_images = []
my_dir = sys.argv[1]
if not os.path.exists("scanned"):
    os.makedirs("scanned")
for pictures in os.listdir(my_dir):
    if os.path.splitext(pictures)[-1].lower() == ".jpg":
        way = my_dir + "/" + pictures
        print(way)
        image = cv2.imread(way)
        ratio = image.shape[0] / 2000.0
        orig = image.copy()
        
        image = imutils.resize(image, height=2000)
        # convert the image to grayscale, blur it, and find edges
        # in the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)
        print("STEP 1: Edge Detection")
        
        # find the contours in the edged image, keeping only the
        # largest ones, and initialize the screen contour
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
        
        # loop over the contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # if our approximated contour has four points, then we
            # can assume that we have found our screen
            if len(approx) == 4:
                screenCnt = approx
                break
        print("STEP 2: Find contours of paper")
        
        # apply the four point transform to obtain a top-down
        warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
        # convert the warped image to grayscale, then threshold it
        # to give it that 'black and white' paper effect
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        T = threshold_local(warped, 15, offset=15, method="gaussian")
        warped = (warped > T).astype("uint8") * 255
        adjusted = cv2.convertScaleAbs(warped, alpha=2, beta=0)
        print("STEP 3: Apply perspective transform")
        
        new_way = "scanned/" + "scanned_" + pictures
        cv2.imwrite(new_way, imutils.resize(adjusted, height=2000))
        my_images.append(new_way)

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(my_images))
