def decimalize(n):
    i=0
    while i*i<n:
        i+=1
    if i*i==n:
        return 0
    num = i-1
    count = 1
    total=i-1
    while count < 100:
        num = num*10
        i=0
        while (num + i) ** 2 < n * (100**count):
            i+=1
        num+=i-1
        total+=i-1
        count+=1
    return total
    
total=0

for i in range(2,100):
    total+=decimalize(i)
print(total)
