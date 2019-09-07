def isPan(num):
    numlist=[]
    for n in str(num):
        if int(n) in numlist:
            return False
        if int(n)==0:
            return False
        numlist.append(int(n))

    if len(numlist)==9:
        return True

for i in range(9000,10000):
    total = int(str(i)+str(i*2))
    if isPan(total):
        print(total)
