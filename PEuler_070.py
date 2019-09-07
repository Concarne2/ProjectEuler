primes = [2,3]

def newDigits():
    digits=[0,0,0,0,0,0,0,0,0,0]
    return digits
def findDigits(n):
    digits = newDigits()
    strn = str(n)
    for c in strn:
        digits[int(c)] += 1
    return digits
def isPrime(n):
    i=0
    while primes[i]*primes[i] <= n:
        if n%primes[i] == 0:
            return False
        i+=1
    primes.append(n)
    return True

MAX = 10000000
minimum = 1000
minnum = 0
for n in range(4,3163):
    isPrime(n)

for p in reversed(primes):
    num = p*p
    while num < MAX:
        totient = int(num/p)*(p-1)
        if findDigits(num) == findDigits(totient):
            '''ratio = num/totient
            if ratio < minimum:
                minimum = ratio
                minnum = orgnum'''
            print(succ)
        num = num * p
        '''
        i = 0
        divisors = []
        appended = False
        while primes[i] <= n:
            if n%primes[i] == 0:
                n = int(n / primes[i])
                if not appended:
                    divisors.append(primes[i])
                    appended = True
            else:
                i+=1
                appended = False
        totient = orgnum
        for p in divisors:
            totient = int(totient / p) * (p-1)
            
        if findDigits(orgnum) == findDigits(totient):
            ratio = orgnum/totient
            if ratio < minimum:
                minimum = ratio
                minnum = orgnum'''
                
print(minnum)
