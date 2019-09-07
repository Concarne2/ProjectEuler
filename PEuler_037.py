primelist=[]

truncs=[]

def isPrime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def checkTrunc(n):
    numstr=str(n)
    for i in range(0,len(numstr)):
        if not primelist[int(numstr[i:len(numstr)])]:
            return False
        if not primelist[int(numstr[0:len(numstr)-i])]:
            return False
    return True

for i in range(0,10):
    primelist.append(False)
primelist[2]=True
primelist[3]=True
primelist[5]=True
primelist[7]=True

num=10
while len(truncs)<11:
    if isPrime(num):
        primelist.append(True)
    else:
        primelist.append(False)
    if primelist[num]:
        if checkTrunc(num):
            truncs.append(num)
    num+=1
