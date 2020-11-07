#/usr/bin/env python

# Install OpenCV and numpy
#$ pip install opencv-python numpy
#import sys
#sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2
import numpy as np
import math
from PIL import Image
from PIL import ImageStat
import time
import os

#minsquare = 60
#images = [img,img2,img3]
#foreach i in images
#  if(w = minsquare)
#    Success -> Stop for minute etc
cv2.namedWindow("opencv")
imageFolder = "images"

#images = ["images/image1.png","images/image2.png","images/image3.png","images/image4.png","images/image5.png","images/image6.png", "images/image7.png"]

imageNames = os.listdir(imageFolder)
images = []
for i in imageNames:
  images.append("images/" + i)
print(imageNames)
print(images)
#range in which we are happy with the camera angle
minSize = 95 
maxSize = 96

#colors for printing sugars
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def timerInterval(interval):
  start_time = time.time()
  interval = 1
  for i in range(len(images)):
      time.sleep(start_time + i*interval - time.time()+0.1)
      square = count_green(images[i])
      imbrightness(images[i])
      if square > minSize and square < maxSize:
        print(bcolors.OKGREEN + "CORRECT POSITION - KEEP POSITION" + bcolors.ENDC)
        break
      print(bcolors.WARNING + "DRONE POSITION NOT CENTERED" + bcolors.ENDC)
    
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
  print(bcolors.OKBLUE + 'The number of green pixels is: ' + str(green)+ bcolors.ENDC)
  w = math.sqrt(green)
  print(bcolors.OKBLUE + 'SQRT DISTANCE is: ' + str(w) + bcolors.ENDC)
  return w  

def imbrightness(image):
  
  im = Image.open(image).convert('L') #you can pass multiple arguments in single line
  #print(type(im))
  stat = ImageStat.Stat(im)
  #im = np.array(Image.convert('L'))
  #stat = ImageStat.Stat(im)
  bness = stat.mean[0]  
  if (bness < 0.5): 
    print(bcolors.FAIL + 'The brightness is too low (' + bness + '). Increase brightness.' + bcolors.ENDC)
  else:
    print(bcolors.OKCYAN+ 'The brightness is OK' + bcolors.ENDC)
  return stat.mean[0]

timerInterval(0.1)

    
#cv2.namedWindow("opencv")
#cv2.imshow("opencv",img)

# vim: ft=python ts=4 sw=4 expandtab