from screen.grab_screen import grabScreen
from screen.getWindowRegion import getWindowRegion
import cv2 as cv
import numpy as np
import time

def turnToFPS(time):
  fps = 1 / time
  return fps

left, up, right, down = getWindowRegion()

runTime = 0
while True:
  # benchmark Start
  firstTime = time.time()

  img = grabScreen(left, up, right, down)
  img = np.reshape(img.grabScreen(), (img.height, img.width, 4))
  
  key = cv.waitKey(1)
  if key == ord('q'):
    print('The window has been quit!\n')
    break
  cv.imshow('show', img)


  # benchmark End
  lastTime = time.time()
  benchmark = lastTime - firstTime
  runTime = runTime + benchmark
  if runTime > 2:
    fps = '{:.2f}'.format(turnToFPS(benchmark))
    print(str(fps) + ' FPS')
    runTime = 0
