def findDiv(n, dic):
    if n == 1:
        pass
    else:
        for div in range(2,n+1):
            if n % div == 0:
                if div in dic:
                    dic[div]+=1
                else:
                    dic[div]=1
                return findDiv(int(n / div), dic)

def calculateAm(n):
    dic={}
    findDiv(n,dic)
    total=1
    for prime in dic:
        multVal=0
        currMult=1
        for power in range(0,dic[prime]+1):
            multVal += currMult
            currMult *= prime
        total *= multVal
    return total - n

amList=[]
for n in range(2,10000):
    if n not in amList:
        a = calculateAm(n)
        b = calculateAm(a)
        if n == b and a != n:
            amList.append(n)
            amList.append(a)

val=0
for n in amList:
    val += n
print(val)
