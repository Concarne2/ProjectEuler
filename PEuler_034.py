fact={}
fact[0]=1
fact[1]=1

for i in range(2,10):
    fact[i]=fact[i-1]*i

for n in range(10,fact[9]*7):
    numstr=str(n)
    sumval=0
    for num in numstr:
        sumval += fact[int(num)]
    if sumval == n:
        print(n)
