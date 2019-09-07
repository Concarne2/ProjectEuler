a=1
b=1
k=0

numlist = [2,1]

for i in range(1,33):
    numlist.append(2 * i)
    numlist.append(1)
    numlist.append(1)
    
numlist.append(66)
numlist.append(1)

for n in reversed(numlist):
    if k == 0:
        k=1
        continue
    k=n
    numerator = a
    denom = n*a + b
    b = numerator
    a = denom
        
total = 0    
for c in str(a):
    total += int(c)
print(total)
