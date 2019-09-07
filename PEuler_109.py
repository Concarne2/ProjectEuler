combs1={}
combs2={}

LIM = 100
maxDartNum = 20

def Add(n,s, dic):
    if n <= LIM:
        if n in dic:
            dic[n].append(s)
        else:
            dic[n] = [s]

for n in range(1,maxDartNum+1):
    Add(n,"S"+str(n), combs1)
    Add(2*n,"D"+str(n), combs1)
    Add(3*n,"T"+str(n), combs1)
Add(25,"SB",combs1)
Add(50,"DB",combs1)

'''
for n in range(1,21):
    for n2 in range(1,maxDartNum+1):
        if n2 in combs1:
            for s in combs1[n2]:
                if n+n2 not in combs2 or (n+n2 in combs2 and "S"+str(n)+s not in combs2[n+n2]):
                    Add(n + n2, s + "S"+str(n), combs2)
                if 2*n+n2 not in combs2 or (2*n+n2 in combs2 and "D"+str(n)+s not in combs2[2*n+n2]):
                    Add(2*n + n2, s + "D"+str(n), combs2)
                if 3*n+n2 not in combs2 or (3*n+n2 in combs2 and "T"+str(n)+s not in combs2[3*n+n2]):
                    Add(3*n + n2, s + "T"+str(n), combs2)
'''
for n in range(1,maxDartNum+1):
    for n2 in combs1:
        for s in combs1[n2]:
            if not (n+n2 in combs2 and "S"+str(n)+s in combs2[n+n2]):
                Add(n + n2, s + "S"+str(n), combs2)
            if not (2*n+n2 in combs2 and "D"+str(n)+s in combs2[2*n+n2]):
                Add(2*n + n2, s + "D"+str(n), combs2)
            if not (3*n+n2 in combs2 and "T"+str(n)+s in combs2[3*n+n2]):
                Add(3*n + n2, s + "T"+str(n), combs2)
for n2 in combs1:
    for s in combs1[n2]:
        if not (25+n2 in combs2 and "SB"+s in combs2[25+n2]):
            Add(25 + n2, s + "SB", combs2)
        if not (50+n2 in combs2 and "DB"+s in combs2[50+n2]):
            Add(50 + n2, s + "DB", combs2)


target = 170

def CountFromTarget(target):
    count = 0
    if target %2 == 0 and target <= 2*maxDartNum:
        count+=1
    if target == 50:
        count+=1
    n = 1

    while target >= 2*n and n<=maxDartNum:
        if target - 2*n in combs1:
            count += len(combs1[target - 2*n])
        if target - 2*n in combs2:
            count += len(combs2[target - 2*n])
        n+=1
    if target - 50 in combs1:
        count += len(combs1[target - 50])
    if target - 50 in combs2:
        count += len(combs2[target - 50])
    return count

total = 0
for t in range(2,100):
    total += CountFromTarget(t)
print(total)





    
