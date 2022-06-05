import win32gui
import sys

def getWindowRegion():
  # WINDOW_TITLE = 'Grand Theft Auto V'
  WINDOW_TITLE = 'test.txt - 记事本'
  window = win32gui.FindWindow(None, WINDOW_TITLE)    
  # 监控的窗口需要运行在窗口状态


  if not window:
    print('ERROR!!')
    print('Please make sure the window has been opened, and resume the program!!\n')
    sys.exit()
  else:
    win32gui.SetForegroundWindow(window)

  # 判断屏幕是否进行了缩放

  # 获取的屏幕位置为四个，分别是左上右下
  pos = (win32gui.GetWindowRect(window))
  if (pos[0] or pos[1] or pos[2] or pos[3]) < 0:
    print('ERROR!!\n')
    print('Can not find the window you want\n')
    sys.exit()

  return pos

if __name__ == '__main__':
  getWindowRegion()