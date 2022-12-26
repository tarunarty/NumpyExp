import numpy as np
n = int(input())
lis = []
for _ in range(n):
    lis.append(input().split())
lis = np.array(lis)
m = int(input())
wrdLst = []
for __ in range(m):
    wrdLst.append(input())
#Check Diagonal

wrdInLst = []

for i in range(n):
    if n-i-1!=0:
        wrd = ""
        for k1 in range(n-i-1):
            wrd += lis[i+k1][k1]
        for w in wrdLst:
            if w in wrd or w[::-1] in wrd:
                wrdInLst.append(w)
    else:
        for j in range(n):
            wrd = ""
            for k2 in range(n-j):
                wrd += lis[k2][j+k2]
        for w in wrdLst:
            if w in wrd or w[::-1] in wrd:
                wrdInLst.append(w)

# check rows and columns

i=0
j=0

for i in range(n):
    for w in wrdLst:
        if w in "".join(lis[i,:]) or w[::-1] in "".join(lis[i,:]) or w in "".join(lis[:,i]) or w[::-1] in "".join(lis[:,i]):
            wrdInLst.append(w)
print(wrdInLst)













        
