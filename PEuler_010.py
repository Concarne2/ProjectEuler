primeList=[2]


def checkPrime(num):
    div = primeList[0]
    index=0
    while div*div <= num:
        if num % div == 0:
            return False
        index+=1
        div=primeList[index]
    return True

sumValue=2
num=3
while num<2000000:
    if checkPrime(num):
        primeList.append(num)
        sumValue += num
    num+=2

print(sumValue)
    
