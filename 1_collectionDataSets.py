from screen.grab_screen import grabScreen
from screen.getWindowRegion import getWindowRegion
import cv2 as cv
import time
import numpy as np
import os

def turnToFPS(time):
  fps = 1 / time
  return fps

def main():
  START_VALUE = 1

  trainingData = []

  region = ()
  region = getWindowRegion()
  runTime = 0

  fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)
  while os.path.isfile(fileName):
    START_VALUE += 1
    fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)
  print('file from No.{}.'.format(START_VALUE))

  while True:
    # benchmark Start
    firstTime = time.time()

    img = grabScreen(region)
    # 控制帧率
    # time.sleep(0.008)
    # 修改下行使数据能够适应CNN
    # img = cv.resize(img, (480, 270))

    # benchmark End
    lastTime = time.time()
    benchmark = lastTime - firstTime
    runTime = runTime + benchmark
    if runTime > 1:
      fps = '{:.2f}'.format(turnToFPS(benchmark))
      print(str(fps) + ' FPS')
      runTime = 0

    # 向文件写入
    trainingData.append(img)
    if len(trainingData) == 500:
      np.save(fileName, trainingData)
      START_VALUE += 1
      trainingData = []
      print('File {} has SAVED!'.format(START_VALUE))
      fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)

def test():
  region = ()
  region = getWindowRegion()
  runTime = 0

  while True:
    # benchmark Start
    firstTime = time.time()

    img = grabScreen(region)
    # img = cv.resize(img, (480, 270))
    key = cv.waitKey(1)
    if key == ord('q'):
      break
    else:
      cv.imshow('show', img)

    # benchmark End
    lastTime = time.time()
    benchmark = lastTime - firstTime
    runTime += benchmark
    if runTime > 1:
      fps = '{:.2f}'.format(turnToFPS(benchmark))
      print('{} FPS         '.format(str(fps)), end='\r')
      runTime = 0


# main()
test()