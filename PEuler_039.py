
maxp=0
maxcount=0

for p in range(12,1001):
    count=0
    for a in range(3,int(p//3.4)):
        val1 = (a*a) % (p-a)
        if val1 != 0:
            continue
        if (p - a + val1) % 2 == 0:
            count+=1
    if count >= maxcount :
        print(p)
        print(count)
        maxp=p
        maxcount=count
            
