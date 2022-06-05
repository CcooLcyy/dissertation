import win32gui
import sys


  


titleTage = True
window = None

def getWindowRegion():
  global titleTage
  global window

  while not window:
    if titleTage == True:
      WINDOW_TITLE = 'Grand Theft Auto V'
      titleTage = False
    window = win32gui.FindWindow(None, WINDOW_TITLE)





  # if titleTage == True:
  #   WINDOW_TITLE = 'test.txt - 记事本'
  #   if WINDOW_TITLE == '':
  #     print('输入标题栏名称啊喂！！！！')
  #     sys.exit()
    
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