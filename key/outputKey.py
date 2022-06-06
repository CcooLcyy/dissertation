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
  keys = keyCheck()
  if 'W' in keys and 'A' in keys:
      output = waKey
  elif 'W' in keys and 'D' in keys:
      output = wdKey
  elif 'S' in keys and 'A' in keys:
      output = saKey
  elif 'S' in keys and 'D' in keys:
      output = sdKey
  elif 'W' in keys:
      output = wKey
  elif 'S' in keys:
      output = sKey
  elif 'A' in keys:
      output = aKey
  elif 'D' in keys:
      output = dKey
  else:
      output = voidKey
  return output
