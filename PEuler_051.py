primes=[False,False,True,True,False]

def isprime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def replaces(n,pos1,pos2,pos3):
    replaces=[]
    nstr=str(n)
    for i in range(0,10):
        if i == 0 and pos1 == 0:
            continue
        replaces.append(int(nstr[:pos1]+str(i)+nstr[pos1+1:pos2]+str(i)+nstr[pos2+1:pos3]+str(i)+nstr[pos3+1:]))
    return replaces
def replaces2(n,pos1,pos2):
    replaces=[]
    nstr=str(n)
    for i in range(0,10):
        if i == 0 and pos1 == 0:
            continue
        replaces.append(int(nstr[:pos1]+str(i)+nstr[pos1+1:pos2]+str(i)+nstr[pos2+1:]))
    return replaces

def countprimes(replacedlist):
    count = 0
    for rep in replacedlist:
        if primes[rep]:
            count += 1
    return count

def trythis(n):
    maxcount=0
    how=""
    replacedlist = replaces(n,0,1,2)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="012"
    replacedlist = replaces(n,0,1,3)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="013"
    replacedlist = replaces(n,0,1,4)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="014"
    replacedlist = replaces(n,0,2,3)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="023"
    replacedlist = replaces(n,0,2,4)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="024"
    replacedlist = replaces(n,0,3,4)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="034"
    replacedlist = replaces(n,1,2,3)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="123"
    replacedlist = replaces(n,1,2,4)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="124"
    replacedlist = replaces(n,1,3,4)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="134"
    replacedlist = replaces(n,2,3,4)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        how="234"
    '''
    replacedlist = replaces2(n,2,3)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        
    replacedlist = replaces(n,0,1,3)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
    replacedlist = replaces(n,0,2,3)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
    replacedlist = replaces(n,1,2,3)
    count = countprimes(replacedlist)
    if maxcount < count:
        maxcount = count
        '''
    if maxcount >= 8:
        print(how)
        return True
    else:
        return False

    
for n in range(5,1000000):
    if isprime(n):
        primes.append(True)
    else:
        primes.append(False)

for n in range(100000,1000000):
    if primes[n]:
        if trythis(n):
            print(n)
            break
    if n%1000==0:
        print(str(n)+"... searching")
