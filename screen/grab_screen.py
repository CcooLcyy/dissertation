from turtle import width
from screen.getWindowRegion import getWindowRegion
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

def grabScreen(region):
  left, up, right, down = region

  left = int(left * getRate()) + 10
  up = int(up * getRate()) + 40
  right = int(right * getRate()) - 10
  down = int(down * getRate()) - 10
  width = right -left + 1
  height = down - up + 1

  hwin = win32gui.GetDesktopWindow() 
  # 从窗口句柄获取设备上下文
  hwindc = win32gui.GetWindowDC(hwin)
  # 从句柄创建设备上下文
  srcdc = win32ui.CreateDCFromHandle(hwindc)
  # 为设备双下文创建内存
  memdc = srcdc.CreateCompatibleDC()
  bmp = win32ui.CreateBitmap()
  bmp.CreateCompatibleBitmap(srcdc, width, height)
  memdc.SelectObject(bmp)
  memdc.BitBlt((0, 0), (width, height), srcdc, (left, up), win32con.SRCCOPY)
  
  signedIntsArray = bmp.GetBitmapBits(True)
  img = np.frombuffer(signedIntsArray, dtype = 'uint8')
  img.shape = (height,width,4)

  srcdc.DeleteDC()
  memdc.DeleteDC()
  win32gui.ReleaseDC(hwin, hwindc)
  win32gui.DeleteObject(bmp.GetHandle())

  return img