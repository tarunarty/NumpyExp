import numpy as np
n = input()
lis = []
for _ in range(int(n.split()[0])):
    lis.append(input().split())
lis = np.array(lis)
t = []
for i in range(len(lis)):
    for j in range(len(lis[0])):
        if lis[i,j] == "$":
            t.append((i,j))
for e in t:
    i,j = e
    lis[i,:] = "$"
    lis[:,j] = "$"

for elem in lis:
    print(" ".join(elem))
