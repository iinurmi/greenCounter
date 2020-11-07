#/usr/bin/env python

# Install OpenCV and numpy
#$ pip install opencv-python numpy
#import sys
#sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2
import numpy as np
import math
import time
#minsquare = 60
#images = [img,img2,img3]
#foreach i in images
#  if(w = minsquare)
#    Success -> Stop for minute etc
cv2.namedWindow("opencv")

images = ["images/image1.png","images/image2.png","images/image3.png","images/image4.png","images/image5.png","images/image6.png", "images/image7.png"]
#range in which we are happy with the camera angle
minSize = 95 
maxSize = 96

def timerInterval(interval):
  start_time = time.time()
  interval = 1
  for i in range(len(images)):
      time.sleep(start_time + i*interval - time.time()+0.1)
      square = count_green(images[i])
      if square > minSize and square < maxSize:
        print("correct position for camera")
        break
    


def count_green(image):
  img = cv2.imread(image)
  cv2.imshow("opencv",img)
  cv2.waitKey(1)
  # minimum value of green pixels
  GREEN_MAX = np.array([100, 255, 200], np.uint8)
  # maximum value of green pixels
  GREEN_MIN = np.array([0, 100, 177], np.uint8)

  dst = cv2.inRange(img, GREEN_MIN, GREEN_MAX)
  green = cv2.countNonZero(dst)
  print('The number of green pixels is: ' + str(green))
  w = math.sqrt(green)
  print('Squareroot(width/height) is: ' + str(w))
  return w 
#for i in images:
#  square = count_green(i)
#  if square > minSize and square < maxSize:
#    print("correct position for camera")
#    break



timerInterval(0.1)


    
#cv2.namedWindow("opencv")
#cv2.imshow("opencv",img)


# vim: ft=python ts=4 sw=4 expandtab