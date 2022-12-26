import numpy as np
def isConcave(a,b):
    x1,y1,x2,y2 = tuple(a)
    x3,y3,x4,y4 = tuple(b)
    ar1 = abs(np.linalg.det([[1,x1,y1],[1,x2,y2],[1,x3,y3]]))
    ar2 = abs(np.linalg.det([[1,x2,y2],[1,x3,y3],[1,x4,y4]]))
    ar3 = abs(np.linalg.det([[1,x3,y3],[1,x4,y4],[1,x1,y1]]))
    ar4 = abs(np.linalg.det([[1,x4,y4],[1,x1,y1],[1,x2,y2]]))
    if round(ar1)+round(ar4)==round(ar2)+round(ar3):
        return True
    else:
        return False

n = int(input())
lis = list(map(int , input().split()))
lis2 = []
for _ in range(int(len(lis)/4)):
    t = tuple(lis[_:_+4])
    del lis[_:_+3]
    lis2.append([t])
lis = lis2
c = 0
lis3 = []
p = 0
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if isConcave(lis[i][0],lis[j][0]):
            c+=1
            x1,y1,x2,y2=lis[i][0]
            x3,y3,x4,y4=lis[j][0]
            x0 = (x1*x4*y2 +x2*x3*y1 + x4*x2*y3 + x1*x3*y4 - x3*x2*y4 - x1*x4*y3 - x3*x1*y2 - x2*x4*y1)/(y2*x4 + y1*x3 + y4*x1 + y3*x2 - x3*y2 - y1*x4 - y4*x2 - y3*x1)
            y0 = (y1*y4*x2 +y2*y3*x1 + y4*y2*x3 + y1*y3*x4 - y3*y2*x4 - y1*y4*x3 - y3*y1*x2 - y2*y4*x1)/(x2*y4 + x1*y3 + x4*y1 + x3*y2 - y3*x2 - x1*y4 - x4*y2 - x3*y1)
            lis3.append([round(x0,2),round(y0,2)])
    p+=1
print(c)
for elem in lis3:
    print(" ".join(list(map(str,elem))))
