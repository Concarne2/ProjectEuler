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
    return result -1

mx=0
for n in range(2,1000001):
    val = n/(n-calculateDiv(n))
    print(str(n)+" "+str(val))
    if val>mx:
        mx=val
