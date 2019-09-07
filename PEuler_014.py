def tryThis(num):
    count=1
    while num>1:
        if num%2 == 0:
            num = num/2
        else:
            num=3*num+1
        count+=1
    
    return count

maxVal=0
for i in range(1,1000000):
    val = tryThis(i)
    if val > maxVal:
        maxVal = val
        print(i)

