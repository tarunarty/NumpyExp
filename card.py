import numpy as np
n = int(input())
lis = []
lis1 = ["H","D","C","S"]
lis2 = ["J","Q","K","A"]
lisNot = []
for _ in range(2,11):
    lis2.append(str(_))

for __ in range(n):
    lis.append(input().split())
lis = list(np.array(lis).reshape(1,-1))

for i in lis1:
    for j in lis2:
        card = j+i
        if card in "".join(lis[0]):
            pass
        else:
            lisNot.append(card)
print(lisNot)
