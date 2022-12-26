R = 4
C = 4
import sys
lis = []
for _ in range(4):
    lis.append(list(map(int,input().split())))

def f(lis,m,n):
    if n<0 or m<0:
        return sys.maxsize
    elif n == 0 and m == 0:
        return lis[m][n]
    else:
        return min(f(lis,m-1,n) , f(lis,m,n-1) , f(lis,m-1,n-1)) + lis[m][n]
print(f(lis,4,4))
