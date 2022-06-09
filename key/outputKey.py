from numpy import void
from key.keyCheck import keyCheck

wKey      = [1,0,0,0,0,0,0,0,0]
sKey      = [0,1,0,0,0,0,0,0,0]
aKey      = [0,0,1,0,0,0,0,0,0]
dKey      = [0,0,0,1,0,0,0,0,0]
waKey     = [0,0,0,0,1,0,0,0,0]
wdKey     = [0,0,0,0,0,1,0,0,0]
saKey     = [0,0,0,0,0,0,1,0,0]
sdKey     = [0,0,0,0,0,0,0,1,0]
voidKey   = [0,0,0,0,0,0,0,0,1]

outputKey = [0,0,0,0,0,0,0,0,0]

def getArrayOfKey():
  '''
  获取方向按键，并且将按键以array的形式返回
  '''
  keys = keyCheck()
  if ord('W') in keys and ord('A') in keys:
    output = waKey
  elif ord('W') in keys and ord('D') in keys:
    output = wdKey
  elif ord('S') in keys and ord('A') in keys:
    output = saKey
  elif ord('S') in keys and ord('D') in keys:
    output = sdKey
  elif ord('W') in keys:
    output = wKey
  elif ord('S') in keys:
    output = sKey
  elif ord('A') in keys:
    output = aKey
  elif ord('D') in keys:
    output = dKey
  else:
      output = voidKey
  return output
