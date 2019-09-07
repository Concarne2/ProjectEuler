def findRight(d, targetN,targetD):
    return int(targetN/targetD*d) + 1
count = 0
for d in range(5,12001):
    for n in range(findRight(d,1,3),findRight(d,1,2)):
        if d%n != 0:
            count+=1
print(count)
