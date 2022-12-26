""" get input n and print n*n numbers as a spiral """
import numpy as np
k = int(input())
lis = np.zeros((k,k))
i,j = k-1,k-1
K = True
c,l = 0,0
while K:
    lis[i,j] = k*k - c
    if j==k-1+l and i!=-l:
        i-=1
    elif i==-l and j!=-l:
        j-=1
    elif j==-l and i!=k-1+l:
        i+=1
    elif i==k-1+l and j!=k-2+l:
        j+=1
    elif i==k-1+l and j==k-2+l:
        l-=1
        i-=1
    c+=1
    if 0 not in lis:
        K=False
print(lis)
"""
for elem in lis:
    print(" ".join(list(map(str,elem))))
"""
