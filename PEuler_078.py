waylist=[]
for i in range(0,8000):
    waylist.append(0)

for n in range(1,len(waylist)):
    waylist[n]+=1
    for k in range(n,len(waylist)):
        waylist[k] += waylist[k-n]
        
for n in range(0,len(waylist)):
    if waylist[n]%100000 == 0:
        print(n)
