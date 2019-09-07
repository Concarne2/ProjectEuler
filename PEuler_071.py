def findLeft(d, targetN,targetD):
    return int(targetN/targetD*d)

currentN=0
currentD=0
min = 1
for d in range(1000,1000000):
    if d%7 == 0:
        continue
    n = findLeft(d,3,7)
    if (3/7)-(n/d) < min:
        currentN = n
        currentD = d
        min = (3/7)-(n/d)
