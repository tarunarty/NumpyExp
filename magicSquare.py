import matlab
n = 6
i,j = matlab.mgrid[0:n,0:n]
a = matlab.mod(i+j+(n-3)/2,n)
b = matlab.mod(i+2*j-2,n)
m = n*a + b + 1
print(m)
