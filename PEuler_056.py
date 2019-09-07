def digSum(n):
    sums = 0
    nstr = str(n)
    for i in nstr:
        sums += int(i)
    return sums

def digSumMax(n):
    maxm = 0
    num = 1
    for i in range (1,101):
        num *= n
        sumd = digSum(num)
        if sumd > maxm:
            maxm = sumd
    return maxm

maxm = 0

for i in range(2,101):
    if i % 10 == 0:
        continue
    sumd = digSumMax(i)
    if sumd > maxm:
        maxm = sumd
print(maxm)
