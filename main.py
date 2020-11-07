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
import videoToFrames
from webcam import testWebcam

#testWebcam()
#minsquare = 60
#images = [img,img2,img3]
#foreach i in images
#  if(w = minsquare)
#    Success -> Stop for minute etc
input_loc = 'testvideo.MOV'
output_loc = 'frames'
#videoToFrames.video_to_frames(input_loc, output_loc)
cv2.namedWindow("opencv")
imageFolder = "frames"

#images = ["images/image1.png","images/image2.png","images/image3.png","images/image4.png","images/image5.png","images/image6.png", "images/image7.png"]

imageNames = os.listdir(imageFolder)
images = []
for i in imageNames:
  images.append(imageFolder + "/" + i)
images.sort()
print(imageNames)
print(images)
#range in which we are happy with the camera angle
minSize = 260 
maxSize = 330

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
      else:
        print(bcolors.WARNING + "DRONE POSITION NOT CENTERED" + bcolors.ENDC)

def display_text(value, label, img, position):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if position is None:
      position = [20,500]
    bottomLeftCornerOfText = (position[0],position[1])
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2

    distanceS = label+':'+str(round(value, 2))
    cv2.putText(img, distanceS, 
      bottomLeftCornerOfText, 
      font, 
      fontScale,
      fontColor,
      lineType)   
    cv2.imshow("img",img)


def count_green(image):
  img = cv2.imread(image)
  
  # minimum value of green pixels
  GREEN_MAX = np.array([100, 255, 200], np.uint8)
  # maximum value of green pixels
  GREEN_MIN = np.array([0, 100, 177], np.uint8)
  dst = cv2.inRange(img, GREEN_MIN, GREEN_MAX)
  green = cv2.countNonZero(dst)
  print(bcolors.OKBLUE + 'The number of green pixels is: ' + str(green)+ bcolors.ENDC)
  w = math.sqrt(green)
  display_text(w, 'C', img, [20,500])
  print(bcolors.OKBLUE + 'SQRT Size is: ' + str(w) + bcolors.ENDC)
  cv2.imshow("opencv",img)
  cv2.waitKey(1)
  return w  

def imbrightness(image):
  
  im = Image.open(image).convert('L') 
  #print(type(im))
  stat = ImageStat.Stat(im)
  #im = np.array(Image.convert('L'))
  #stat = ImageStat.Stat(im)
  bness = stat.mean[0]  
  display_text(bness, 'Brightness',cv2.imread(image),[20,500])
  if (bness < 0.5): 
    print(bcolors.FAIL + 'The brightness is too low (' + bness + '). Increase brightness.' + bcolors.ENDC)
  else:
    print(bcolors.OKCYAN+ 'The brightness is OK' + bcolors.ENDC)
  return stat.mean[0]

timerInterval(0.1)

    
#cv2.namedWindow("opencv")
#cv2.imshow("opencv",img)

# vim: ft=python ts=4 sw=4 expandtab