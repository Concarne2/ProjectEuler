import numpy as np

maxsol=0
maxD=0

for D in range(0,100):
    print(D)
    sqrtd=np.sqrt(D)
    if sqrtd==int(sqrtd):
        continue
    x = int(sqrtd)
    while True:
        if(D==62):
            print(x)
            print(y)
        y = int(x/sqrtd)
        if x*x - D * y * y == 1:
            break
        x+=1
    if x > maxsol:
        maxsol = x
        maxD = D
print(maxD)
print(maxsol)
