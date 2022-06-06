import win32gui, win32print, win32con, win32api
import sys

def getRate():
  hwin = win32gui.GetDC(0)
  # 真实分辨率
  realX = win32print.GetDeviceCaps(hwin, win32con.DESKTOPHORZRES)
  # 缩放之后
  nowX = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
  rate = realX / nowX
  return rate


def getWindowRegion():
  # WINDOW_TITLE = 'Grand Theft Auto V'
  WINDOW_TITLE = 'test.txt - 记事本'
  window = win32gui.FindWindow(None, WINDOW_TITLE)    
  # 监控的窗口需要运行在窗口状态

  if not window:
    print('ERROR!!')
    print('Please make sure the window has been opened, and resume the program!!\n')
    sys.exit()
  # 将需要监视的窗口置顶。
  # else:
  #   win32gui.SetForegroundWindow(window)

  # 获取的屏幕位置为四个，分别是左上右下
  left, up, right, down = (win32gui.GetWindowRect(window))
  pos = int(left*getRate() + 10), int(up*getRate() + 40), int(right*getRate() - 10), int(down*getRate() - 10)
  if (pos[0] or pos[1] or pos[2] or pos[3]) < 0:
    print('ERROR!!\n')
    print('Can not find the window you want\n')
    sys.exit()
  return pos

if __name__ == '__main__':
  getWindowRegion()