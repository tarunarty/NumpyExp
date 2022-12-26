"""Lol . Spiral using numpy is so easy..."""
import numpy as np
k = int(input())
l = []
for i in range(k):
    l.append(list(input()))
lis = np.array(l)
i = 0
if(k%2 == 1):
    lisSpiral = []
    for i in range(2*k - 1):
        if(i%4 == 0):
            lisRow = lis[0,:]
            lis = np.delete(lis , 0 , axis = 0)
            lisSpiral.append(lisRow)
        elif(i%4 == 1):
            lisCol = lis[:,len(lis[0])-1]
            lis = np.delete(lis , len(lis[0])-1 , axis = 1)
            lisSpiral.append(lisCol)
        elif(i%4 == 2):
            lisRowRev = list(lis[len(lis[0])-1,:])
            lisRowRev.reverse()

            lis = np.delete(lis , len(lis[0])-1 , axis = 0)
            lisSpiral.append(lisRowRev)
        else:
            lisColRev = list(lis[:,0])
            lisColRev.reverse()
            
            lis = np.delete(lis , 0 , axis = 1)
            lisSpiral.append(lisColRev)

if(k%2 == 0):
    lisSpiral = []
    for i in range(2*k):
        if(i%4 == 0):
            lisRow = lis[0,:]
            lis = np.delete(lis , 0 , axis = 0)
            lisSpiral.append(lisRow)
        elif(i%4 == 1):
            lisCol = lis[:,len(lis[0])-1]
            lis = np.delete(lis , len(lis[0])-1 , axis = 1)
            lisSpiral.append(lisCol)
        elif(i%4 == 2):
            lisRowRev = list(lis[len(lis[0])-1,:])
            lisRowRev.reverse()

            lis = np.delete(lis , len(lis[0])-1 , axis = 0)
            lisSpiral.append(lisRowRev)
        else:
            lisColRev = list(lis[:,0])
            lisColRev.reverse()
            
            lis = np.delete(lis , 0 , axis = 1)
            lisSpiral.append(lisColRev)


            

        
