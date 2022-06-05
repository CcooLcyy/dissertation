from screen.grab_screen import grabScreen
import cv2 as cv
import numpy as np
import time

def turnToFPS(time):
  fps = 1 / time
  return fps


while True:
  # benchmark Start
  firstTime = time.time()


  img = grabScreen()
  img = np.reshape(img.grabScreen(), (img.height, img.width, 4))
  
  key = cv.waitKey(1)
  if key == ord('q'):
    print('The window has been quit!\n')
    break
  cv.imshow('show', img)


  # benchmark End
  lastTime = time.time() - firstTime
  fps = '{:.2f}'.format(turnToFPS(lastTime))
  print(str(fps) + ' FPS')
