
primes=[2,3,5,7]

def isprime(n):
    i=0
    while primes[i] * primes[i] <=n:
        if n % primes[i] == 0:
            return False
        i += 1
    primes.append(n)
    return True

num=9
while True:
    num+=2
    isit=True
    if not isprime(num):
        n = 1
        while 2*n*n < num:
            if num - 2*n*n in primes:
               isit = False
            n += 1
    else:
        continue
    if isit:
        print(num)
        break
