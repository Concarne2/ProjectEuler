arrivals=[]
arrivals.append(True)

def calculate(n):
    nstr=str(n)
    total=0
    for s in nstr:
        total+=(int(s)*int(s))
    return total

for n in range(1,7*81+1):
    res = n
    while True:
        if res == 1:
            arrivals.append(False)
            break
        elif res == 89:
            arrivals.append(True)
            break
        res = calculate(res)

count=0
for n in range(1,10000001):
    if(arrivals[calculate(n)]):
        count+=1

print(count)
