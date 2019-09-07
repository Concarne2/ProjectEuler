primes = [2,3]
def isPrime(n):
    i=0
    while primes[i]*primes[i] <= n:
        if n%primes[i] == 0:
            return False
        i+=1
    primes.append(n)
    return True

'''
for i in range(5,1000000):
    isPrime(i)
'''
count = 0
MAX = 1000000

for i in range(2,500001):
    count += MAX//i * 
