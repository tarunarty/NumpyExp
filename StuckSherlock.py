import numpy as np
for _ in range(int(input())):
    n = int(input())
    lis = []
    for i in range(n):
        lis.append(list(input()))
    lis = np.array(lis)
    mirror = 0
    for i in range(n):
        for j in range(n):
            if lis[:,j] == ["."]*n and lis[i,j:n] == ["."]*(n-j):
                mirror += 1
    print(mirror)
