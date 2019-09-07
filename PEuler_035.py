primelist=[]
MAX=1000000

def isPrime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

primelist.append(False)
primelist.append(False)
for i in range(2,MAX):
    primelist.append(isPrime(i))

def checkCirc(n):
    if not primelist[n]:
        return False
    nstr=str(n)
    for i in range(0,len(nstr)):
        nstr=nstr[len(nstr)-1]+nstr[0:len(nstr)-1]
        if not primelist[int(nstr)]:
            return False
    return True

count=0
for i in range(2,MAX):
    if primelist[i]:
        if checkCirc(i):
            count+=1
