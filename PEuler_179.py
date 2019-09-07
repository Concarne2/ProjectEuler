primes=[2]

def CountDivs(n):
    count = 1
    i = 0
    divd = 0
    while primes[i] * primes[i] <= n:
        while n % primes[i] == 0:
            divd += 1
            n = n / primes[i]
        else:
            count = count * (divd+1)
            divd = 0
            i += 1
    count = count * (divd+1)
    if n != 1:
        count *= 2
    if count == 1:
        count+=1
    return count

for n in range(3,10000):
    i = 0
    isprime = True
    while primes[i] * primes[i] <= n:
        if n % primes[i] == 0:
            isprime = False
            break
        i+=1
    if isprime:
        primes.append(n)

div1 = 2
div2 = 0
count = 0
for n in range(3,10**7):
    div2 = CountDivs(n)
    if div1 == div2:
        count+=1
    div1 = div2
