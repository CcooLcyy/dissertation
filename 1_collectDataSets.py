from key.keyCheck import keyCheck
from screen.grab_screen import grabScreen
from key.outputKey import getArrayOfKey
import cv2 as cv
import time
import numpy as np
import os

def turnToFPS(time):
  fps = 1 / time
  return fps

def main():
  paused = False
  START_VALUE = 1


  # trainingData = []
  trainingData = np.asanyarray([], dtype=object)

  # 进行预处理
  runTime = 0

  # 处理文件路径与文件名
  fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)
  while os.path.isfile(fileName):
    START_VALUE += 1
    fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)

  print('file from No.{}.'.format(START_VALUE), end='\r')
  time.sleep(2)
  print('We will start now !!\n', end='\r')
  time.sleep(2)

  while True:
    if not paused:
      # benchmark Start
      firstTime = time.time()

      # 处理屏幕
      img = grabScreen()
      # 控制帧率
      time.sleep(0.007)
      # 修改下行使数据能够适应CNN
      # img = cv.resize(img, (480, 270))
      
      img = cv.Canny(img, 1, 1)
      cv.imshow('show', img)
      
      # 处理键盘输入
      outputKey = getArrayOfKey()

      # benchmark End
      lastTime = time.time()
      benchmark = lastTime - firstTime
      runTime = runTime + benchmark
      if runTime > 1:
        fps = '{:.2f}'.format(turnToFPS(benchmark))
        print('{} FPS         '.format(str(fps)), end='\r')
        runTime = 0

      # 向文件写入
      trainingData = np.append(trainingData, [img, outputKey])
      if len(trainingData) == 1000:
        np.save(fileName, trainingData)
        trainingData = []
        print('File {} has SAVED!             '.format(START_VALUE))
        START_VALUE += 1
        fileName = './trainingDatas/trainingData-{}.npy'.format(START_VALUE)

    key = keyCheck()
    if ord('T') in key:
      if paused:
        paused = False
        print('继续            ', end='\r')
        time.sleep(1)
      else:
        paused = True
        print('暂停            ', end='\r')
        time.sleep(1)

main()