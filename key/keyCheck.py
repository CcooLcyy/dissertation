import win32api

#   return keyList
# def makeKeyboard():
keyList = []
for ASCII in range(32, 127, 1):
  key = ASCII
  keyList.append(key)

def keyCheck():  
  '''
  如果按下的键在keyList中，那么就将这些按键的ASCII传入列表中
  返回列表
  '''
  keys = []
  for key in keyList:
    if win32api.GetAsyncKeyState(key):
      keys.append(key)
  return keys