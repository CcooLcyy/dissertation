from fileinput import filename
from screen.grab_screen import grabScreen
from screen.getWindowRegion import getWindowRegion
import cv2 as cv
import time
import numpy as np
import os

def turnToFPS(time):
  fps = 1 / time
  return fps

START_VALUE = 1

trainingData = []

left, up, right, down = getWindowRegion()
runTime = 0

fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)
while os.path.isfile(fileName):
  START_VALUE += 1
  fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)
print('file from {}.'.format(START_VALUE))

while True:
  # benchmark Start
  firstTime = time.time()
  

  img = grabScreen(left, up, right, down).grabScreen()
  img = cv.resize(img, (480, 270))
  trainingData.append(img)

  if len(trainingData) % 100 == 0:
    print(len(trainingData))
  if len(trainingData) == 500:
    np.save(fileName, trainingData)
    START_VALUE += 1
    trainingData = []
    print('Data has SAVED!')
    fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)

  # benchmark End
  lastTime = time.time()
  benchmark = lastTime - firstTime
  runTime = runTime + benchmark
  if runTime > 1:
    fps = '{:.2f}'.format(turnToFPS(benchmark))
    print(str(fps) + ' FPS')
    runTime = 0
