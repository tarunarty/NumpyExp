import numpy as np
lis = []
for _ in range(int(input())):
    lis.append(list(map(int , input().split())))
lis = np.array(lis)
lisSum = []
for p in range(len(lis)):
    i = p
    j = 0
    s = 0
    while i<len(lis):
        s += lis[i,j]
        i+=1
        j+=1
    lisSum.append(s)
print(max(lisSum))
