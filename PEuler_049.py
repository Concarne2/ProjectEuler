primes=[2]

MAX = 10000

start = -1

for n in range(3,MAX):
    i=0
    isprime=True
    while True:
        p = primes[i]
        if p*p>n:
            break
        if n%p == 0:
            isprime = False
            break
        i+=1
    if isprime:
        if start == -1 and n > 1000:
            start = len(primes)
        primes.append(n)
        

def isprime(n):
    for p in primes:
        if p==n:
            return True
        if p>n:
            return False

def rearrange(n,f,s):
    arr=[]
    for st in str(n):
        arr.append(int(st))
    temp = arr[f-1]
    arr[f-1]=arr[s-1]
    arr[s-1]=temp
    ns = ""
    for a in arr:
        ns = ns+str(a)
    return int(ns)

def isperm(n1,n2):
    permlist1=[]
    permlist2=[]
    for i in range(0,10):
        permlist1.append(0)
        permlist2.append(0)
    for s in str(n1):
        permlist1[int(s)]+=1
    for s in str(n2):
        permlist2[int(s)]+=1
    return permlist1==permlist2


def isdiff(n):
    ns = str(n)
    for i in range(0,len(ns)-1):
        for j in range(i+1,len(ns)):
            if ns[i] == ns[j]:
                return False
    return True

def isordered(n):
    ns = str(n)
    for i in range(0,len(ns)-1):
        if int(ns[i]) > int(ns[i+1]):
            return False
    return True
''''
for n in primes[start:]:
    if not isdiff(n):
        continue
    
    print(n)'''

for i in range(start,len(primes)):
    for j in range(i+1,len(primes)):
        if (primes[j] + primes[j] - primes[i]) > 10000:
            break
        if (primes[j] + primes[j] - primes[i]) in primes:
            if isperm (primes[i],primes[j]) and isperm(primes[i],primes[j] + primes[j] - primes[i]):
                print(str(primes[i])+str(primes[j])+str(primes[j] + primes[j] - primes[i]))    

