def isPan(multiplicand,multiplier,product):
    numlist=[]
    for n in str(multiplicand):
        if int(n) in numlist:
            return False
        if int(n)==0:
            return False
        numlist.append(int(n))
    for n in str(multiplier):
        if int(n) in numlist:
            return False
        if int(n)==0:
            return False
        numlist.append(int(n))
    for n in str(product):
        if int(n) in numlist:
            return False
        if int(n)==0:
            return False
        numlist.append(int(n))

    if len(numlist)==9:
        return True

val=[]
for i in range(1,98):
    for j in range(123,9876):
        if(isPan(i,j,i*j)):
            print(str(i)+" "+str(j))
            if i*j not in val:
                val.append(i*j)
sumval=0
for v in val:
    sumval+=v
print(sumval)
