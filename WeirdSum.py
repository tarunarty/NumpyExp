import numpy as np
def f(l):
    c = 0
    for i in range(len(l)):
        if i != len(l) - 1:
            if "X" not in l[i]:
                e = l[i]
                f = e[:len(e)-1]
                t = int(f)
                c += t*(pow(10,len(l)-i-1))
            else:
                pass
        else:
            if l[i] == "E":
                c+=1
            else:
                c+=int(l[i][:len(l[i])-1])
    return c
lis = []
line = input()
while line != "#":
    lis.append(line.split())
    line = input()
lis = np.array(lis)
lis = lis.T
l = []
for e in lis:
    l.append(f(e))
s = str(sum(l))
l2 = []
for i in range(len(s)):
    if i != len(s)-1:
        if s[i] == "0":
            l2.append("X")
        else:
            l2.append(s[i]+"s")
    else:
        if s[i] == "1":
            l2.append("E")
        elif s[i] == "0":
            l2.append("X")
        else:
            l2.append(s[i] + "L")
