maxPal=0

def checkPal(num):
    palStr = str(num)
    isPal = True
    for i in range(0,len(palStr)):
        if palStr[i] != palStr[len(palStr)-1-i]:
            isPal = False
    return isPal

for i in range(100,1000):
    for j in range(100,1000):
        if checkPal(i * j) and i*j>maxPal:
            maxPal = i * j

print(maxPal)
