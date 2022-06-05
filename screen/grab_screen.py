from screen.getWindowRegion import getWindowRegion
# from getWindowRegion import getWindowRegion
# 此文件不应该单独执行，如果需要单独执行，请将此注释上方两条代码更改注释状态（已注释改为未注释，未注释改为已注释）
import win32gui, win32ui, win32con, win32print, win32api
import numpy as np

def getRate():
  hwin = win32gui.GetDC(0)

  # 真实分辨率
  realX = win32print.GetDeviceCaps(hwin, win32con.DESKTOPHORZRES)

  # 缩放之后
  nowX = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
  rate = realX / nowX
  return rate

class GrabScreen():
  def __init__(self, left, up, right, down, width, height):
    self.left = left
    self.up = up
    self.right = right
    self.down = down
    self.width = width
    self.height = height
  def grabScreen(self):
      hwin = win32gui.GetDesktopWindow()
      hwindc = win32gui.GetWindowDC(hwin)
      srcdc = win32ui.CreateDCFromHandle(hwindc)
      memdc = srcdc.CreateCompatibleDC()

      bmp = win32ui.CreateBitmap()
      bmp.CreateCompatibleBitmap(srcdc, self.width, self.height)
      memdc.SelectObject(bmp)
      memdc.BitBlt((0, 0), (self.width, self.height), srcdc, (self.left, self.up), win32con.SRCCOPY)
      # bmp.SaveBitmapFile(memdc, './test.bmp')
      
      arrayFromBuffer = bmp.GetBitmapBits(True)
      img = np.frombuffer(arrayFromBuffer, 'uint8')

      srcdc.DeleteDC() 
      memdc.DeleteDC()
      win32gui.ReleaseDC(hwin, hwindc)
      win32gui.DeleteObject(bmp.GetHandle())

      # !!!TEST:
      # print(img)
      # while True:
      #   key = cv.waitKey(0)
      #   if key == ord('q'):
      #     break
      #   else:
      #     img = np.reshape(img, (height, width, 4))
      #     # 从屏幕获取的图像就是RGB格式无需通过BGR2RGB
      #     # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
      #     img = cv.Canny(img, 1, 1)
      #     print('The shape of img by Canny is ' + str(np.shape(img)))
      #     cv.imshow('show', img)

      return img

def grabScreen(left, up, right, down):
  left = int(left * getRate()) + 10
  up = int(up * getRate()) + 40
  right = int(right * getRate()) - 10
  down = int(down * getRate()) - 10
  WIDTH = right -left + 1
  HEIGHT = down - up + 1

  grabScreen = GrabScreen(left, up, right, down, WIDTH, HEIGHT)
  return grabScreen

if __name__ == '__main__':
  grabScreen()