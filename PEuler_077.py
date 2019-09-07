primes=[2]

for i in range(3,100):
    n = 2
    isprime = True
    while n*n<=i:
        if i%n == 0:
            isprime = False
            break
        n += 1
    if isprime:
        primes.append(i)
        

waylist=[]
for i in range(0,1000):
    waylist.append(0)

goal = 5000
MAX = 0
'''
while MAX < goal:
    newnum = len(waylist)
    newways = 0
    for p in primes:
        if p > newnum:
            break
        if p == newnum:
            newways += 1
        else:
            newways += waylist[newnum - p]
    print(str(newnum) + ", " + str(newways))
    if newways > MAX:
        MAX = newways
    waylist.append(newways)
'''
for p in primes:
    waylist[p]+=1
    for i in range(p+1,len(waylist)):
        waylist[i] += waylist[i-p]
        
