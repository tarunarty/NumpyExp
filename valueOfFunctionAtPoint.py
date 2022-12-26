import numpy as np
n = int(input())
lis = list(map(int , input().split()))
q = int(input())
for _ in range(q):
    print(np.polyval(lis,int(input())))
