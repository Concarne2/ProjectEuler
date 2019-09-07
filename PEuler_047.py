import time
import sys

start_time=time.time()
primes=[2]

MAX = 100000

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

def isprime(n):
    for p in primes:
        if p==n:
            return True
        if p>n:
            return False

def factor(n):
    num = n
    count = 0
    for p in primes:
        if num==1:
            return count
        if p*p>num:
            return count + 1
        if num%p == 0:
            count+=1
            while num%p == 0:
                num = int(num/p)
    return count

count = 0
print('start')
for n in range(2,MAX*10):
    if factor(n) == 4:
        count +=1
        if count>=4:
            print(n)
            print("--- %s seconds ---" % (time.time() - start_time))
            sys.exit()
    else:
        count=0

    
