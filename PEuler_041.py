def isPrime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def isPan(num):
    numlist=[]
    for n in str(num):
        if int(n) in numlist:
            return False
        if int(n)==0 or int(n)==8 or int(n)==9:
            return False
        numlist.append(int(n))

    if len(numlist)==7:
        return True

for n in range(7000000,8000000):
    if isPan(n):
        if isPrime(n):
            print(n)
