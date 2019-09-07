combs=[0,0]

n=2
while True:
    comb = int(n * (n-1) / 2)
    if comb > 2000000/5:
       break
    else:
        combs.append(comb)
    n+=1
    
mindist=10000000
area=-1
pair=(1,1)

i = 4
while combs[i] * combs[i] < 2010000:
    for j in range(i,len(combs)):
        if combs[i]*combs[j]>2000000:
            break
    dist1 = combs[i]*combs[j]-2000000
    dist2 = 2000000-combs[i]*combs[j-1]
    print(dist1)
    print(dist2)
    if dist1<mindist:
        mindist = dist1
        area = combs[i]*combs[j]
        pair=(i,j)
    if dist2<mindist:
        mindist = dist2
        area = combs[i]*combs[j-1]
        pair=(i,j-1)
    i+=1
