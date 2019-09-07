import numpy as np
total = 10**12+1

while True:
    blueD=total//np.sqrt(2)+1
    if blueD * (blueD-1) *2 == total * (total-1):
        break;
    total += 1
print(total)
