currencies=[1,2,5,10,20,50,100,200]

ways=[]
for i in range(0,201):
    ways.append(0)

for c in currencies:
    ways[c]+=1
    for i in range(c+1,201):
        ways[i] += ways[i-c]
    
