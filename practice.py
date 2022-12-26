"""
Get two inputs
k and n
where k is the k-ibonacci sequence number
and n is the numbers of the sequence
to print out.
Done using numpy and matrices.
"""


import numpy as np
import warnings
warnings.filterwarnings('ignore')

k = int(input())
n = int(input())

l = [1] + [-1]*k
lis = np.roots(l)

lis2 = []

for i in range(k):
    l2 = [0]*k
    for j in range(k):
        l2[j] = pow(lis[j],i+1)
    lis2.append(l2)
        
lisRoots = np.array(lis2)
lisSol = np.linalg.solve(lisRoots , np.array([1]*k))

for m in range(1,n):
    s = 0
    for n in range(k):
        s += lisSol[n]*(pow(lis[n] , m))
    print(int(round(s)) , end = " ")

