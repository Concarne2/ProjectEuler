import numpy as np

def calcNext(nums):
    sqnum, addnum, denom = nums

    Ndenom = int((sqnum - addnum*addnum) / denom)

    k = int((np.sqrt(sqnum) - addnum)/Ndenom)

    Naddnum = -1*addnum - k*Ndenom

    return (k,(Naddnum,Ndenom))


totalCount = 0
for n in range(2,10001):
    if int(np.sqrt(n))==np.sqrt(n):
        continue
    k0 = int(np.sqrt(n))

    add_og = -1*k0
    add = add_og

    denom_og = 1
    denom = denom_og

    count = 0
    while True:
        k,(add,denom) = calcNext((n,add,denom))
        count +=1
        if (add,denom) == (add_og,denom_og):
            if count %2 == 1:
                totalCount+=1
            break
            
print(totalCount)
