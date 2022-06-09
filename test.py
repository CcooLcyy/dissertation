import numpy as np 
arr = np.load('./trainingDatas/trainingData-1.npy', allow_pickle=True)


for i in arr:
  for j in arr[i]:
    for k in arr[i][j]:
      print(arr[i][j][k])
