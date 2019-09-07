count = 1
num=1

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

def calculateDiv(n):
    dic={}
    findDiv(n,dic)
    result = 1
    for num in dic.values():
        result *= (num+1)
    return result

'''
def findDiv(n):
    count = 0
    for i in range (1,int(n/2)+1):
        if n % i == 0:
            count += 1
    return count
'''

while True:
    num = int(count * (count + 1) / 2)
    div = calculateDiv(num)
    if div > 500:
        print(num)
        break
    else:
        count+=1
    
