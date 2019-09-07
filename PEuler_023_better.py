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

abun=[]

for n in range(2,28123):
    if n < calculateAm(n):
        abun.append(n)

sumList=[]
for i in range(0,28123*2+1):
    sumList.append(True)
for i in range(0,len(abun)):
    for j in range(i,len(abun)):
        sumList[abun[i]+abun[j]]=False
val=0
for i in range(0,30000):
    if sumList[i]:
        val+=i

        
'''
def tryThis(n):
    index=0
    while abun[index] <= n/2 and index<len(abun):
        if n - abun[index] in abun:
            return False
        index+=1
    return True

val=0
for n in range(1,28123):
    if tryThis(n):
        val += n
    if n%10 == 0:
        print(n)
'''
'''
sumList=[]
for i in range(0,len(abun)):
    for j in range(i,1000):
        val = abun[i] + abun[j]
        if val > 28123:
            break;
        elif val not in sumList:
            sumList.append(val)
'''     
