import win32api

#   return keyList
# def makeKeyboard():
keyList = []
for ASCII in range(32, 127, 1):
  key = ASCII
  keyList.append(key)

def keyCheck():  
  keys = []
  for key in keyList:
    if win32api.GetAsyncKeyState(key):
      keys.append(key)
  return keys


if __name__ == "__main__":
# 测试函数是否运行正常
  while True:
    keys = keyCheck(keys)
    key = ord('Q')
    if key in keys:
      break