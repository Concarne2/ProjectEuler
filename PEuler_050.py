primes=[2]

MAX = 1000000

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
        primes.append(n)
        
def consum(start,end):
    t=0
    for i in range(start-1,end):
       t+=primes[i]
    return t

def isprime(n):
    for p in primes:
        if p==n:
            return True
        if p>n:
            return False

def chain(length):
    count = 0
    total = sum(primes[:length])
    while True:
        if total > MAX:
            return -1
        if isprime(total):
            return count
        total += primes[count + length]
        total -= primes[count]
        count += 1
    
for l in range(500,600):
    res = chain(l)
    if res!=-1:
        print(l)
        print(res)
    
