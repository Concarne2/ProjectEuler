def isperm(n1,n2):
    permlist1=[]
    permlist2=[]
    for i in range(0,10):
        permlist1.append(0)
        permlist2.append(0)
    for s in str(n1):
        permlist1[int(s)]+=1
    for s in str(n2):
        permlist2[int(s)]+=1
    return permlist1==permlist2

for n in range(100000,200000):
    if isperm(n,2*n):
        if isperm(n,3*n):
            print(n)
