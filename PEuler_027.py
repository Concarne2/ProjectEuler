
def isPrime(n):
    if n<=1:
        return False
    i=2
    while i*i<=n:
        if n % i == 0:
            return False
        i+=1
    return True

def quad(a,b,n):
    return n*n+a*n+b

def check(a,b):
    n=0
    val = quad(a,b,n)
    while isPrime(val):
        n+=1
        val=quad(a,b,n)
    return n-1


maxval=0
store=(0,0)
for a in range(-999,1000):
    for b in range(-1000,1001):
        val = check(a,b)
        if val>maxval:
            maxval=val
            store=(a,b)
print(store)
            
