import numpy as np
n,q = tuple(map(int,input().split()))
lis = np.zeros(n*n).reshape(n,n)
for _ in range(q):
    s = input().split()
    if s[0] == "RowAdd":
        lis[int(s[1])-1,:]+=int(s[2])
    else:
        lis[:,int(s[1])-1]+=int(s[2])
print(np.max(lis))
