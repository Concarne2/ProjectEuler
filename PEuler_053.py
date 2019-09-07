fact=[]
fact.append(1)

for i in range(1,101):
    fact.append(i * fact[-1])

def C(n,r):
    return fact[n]/(fact[r]*fact[n-r])

count=0
for n in range(20,101):
    for r in range(1,n):
        if C(n,r) > 1000000:
            count+=1
print(count)
