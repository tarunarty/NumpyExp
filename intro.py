import numpy as np
a = input()
lis = []
lis.append(list(a[0:3]))
lis.append(list(a[3:6]))
lis.append(list(a[6:9]))
print(lis)
A = np.array(lis)
print(A)
R = False
for i in range(3):
    if len(set(lis[i])) == 1:
        R = True
        break
A = A.T
lis = list(A)
C = False
for j in range(3):
    if len(set(lis[j])) == 1:
        C = True
        break
if(lis[0][0] == lis[1][1] == lis[2][2]):
    print("Player " + lis[1][1] + " won.")
elif(lis[2][0] == lis[1][1] == lis[0][2]):
    print("Player " + lis[1][1] + " won.")
elif R == True:
    print("Player " + lis[0][i] + " won.")
elif C == True:
    print("Player " + lis[j][0] + " won.")
elif(C==R==False):
    print("There was a tie.")










