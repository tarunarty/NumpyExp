import numpy as np
lis = []
line = input()
while line != "#":
    lis.append(list(map(int , line.split())))
    line = input()
lis = np.array(lis)
s = sum(lis[0])
S = 0
l = []
for i in range(len(lis)):
    S += lis[len(lis)-i-1,i]
if s == sum(lis.diagonal()):
    if s == S:
        for j in range(len(lis)):
            Sum1 = sum(lis[j])
            Sum2 = sum(lis[:,j])
        if s==Sum1 and s==Sum2:
            pass
        else:
            l = [False]
if len(l)==0 and s == sum(lis.diagonal()) and s == S:
    print("This is a magic square")
else:
    print("This is not a magic square")
