import numpy as np
from itertools import combinations as cb
s = list(input())
del s[0],s[1],s[-1],s[-2]
s = "".join(s)
l = []
for i in range(0,len(s),8):
    l.append(s[i+1:i+6])
n = int(len(l)**(1/2))
lis1 = np.zeros((n,n) , dtype = str)
for elem in l:
    e = "".join(elem).split(",")
    x,y,val = e
    lis1[int(x)-1,int(y)-1] = val
s = list(input())
del s[0],s[1],s[-1],s[-2]
s1 = "".join(s)
l = []
for i in range(0,len(s1),8):
    l.append(s[i+1:i+6])
lis2 = np.zeros((n,n) , dtype = str)
for elem in l:
    e = "".join(elem).split(",")
    x,y,val = e
    lis2[int(x)-1,int(y)-1] = val

al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al = al[:n]
K = True
lis = list(cb(al , 2))
for e in lis:
    a,b = e
    c = 0
    for i in range(n):
        for j in range(n):
            if lis1[i,j] == a and lis2[i,j] == b:
                c+=1
    if c == 1:
        pass
    else:
        break
        K = False
if K:
    print("".join(s))
    














    
