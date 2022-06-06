import win32gui, win32ui, win32con
from screen.getWindowRegion import getWindowRegion
import numpy as np

region = ()
region = getWindowRegion()

def grabScreen():
  left, up, right, down = region
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
  
  arrayFromBuffer = bmp.GetBitmapBits(True)
  img = np.frombuffer(arrayFromBuffer, dtype = 'uint8')
  img.shape = (height,width,4)

  srcdc.DeleteDC()
  memdc.DeleteDC()
  win32gui.ReleaseDC(hwin, hwindc)
  win32gui.DeleteObject(bmp.GetHandle())

  return img