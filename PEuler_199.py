import numpy as np
'''
class circle:
    def __init__(self, k1, k2, k3, outer):
        self.parents=(k1,k2,k3)
        self.isOuter = outer
'''
def descartes(k1,k2,k3):
    return 1 / (k1 + k2 + k3 + 2*np.sqrt(k1*k2 + k2*k3 + k3*k1))

r0 = 1/(1+2/np.sqrt(3))

area = 3 * np.pi * (r0**2)

OCircles_0 = {(r0,r0) : 3}
ICircles_0 = {(r0,r0,r0) : 1}

def loop(OCircles, ICircles, areas):
    newO = {}
    newI = {}

    for (r1,r2), count in OCircles.items():
        r = descartes(1/r1,1/r2,-1)
        areas += count * np.pi * r**2
        if (r1,r) in newO:
            newO[r1,r] += count
        else:
            newO[r1,r] = count
        if (r2,r) in newO:
            newO[r2,r] += count
        else:
            newO[r2,r] = count
        if (r1,r2,r) in newI:
            newI[r1,r2,r] += count
        else:
            newI[r1,r2,r] = count
        
    for (r1,r2,r3), count in ICircles.items():
        r = descartes(1/r1,1/r2,1/r3)
        areas += count * np.pi * r**2
        if (r1,r2,r) in newI:
            newI[r1,r2,r] += count
        else:
            newI[r1,r2,r] = count
        if (r2,r3,r) in newI:
            newI[r2,r3,r] += count
        else:
            newI[r2,r3,r] = count
        if (r3,r1,r) in newI:
            newI[r3,r1,r] += count
        else:
            newI[r3,r1,r] = count
    return newO, newI, areas

OCircles, ICircles, area = loop(OCircles_0, ICircles_0, area)
for i in range(0,9):
    OCircles, ICircles, area = loop(OCircles, ICircles, area)
print(area/np.pi)
