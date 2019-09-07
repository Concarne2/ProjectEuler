def find(n):
    divnum=n
    count=0
    divds=[]
    for i in range(0,n):
        divds.append((0,0))

    power=1
    while 10**power < divnum:
            power += 1
    leftover = 1

    cycleStart = 0
    
    while True:
        if leftover * 10**power % divnum == 0:
            return 0
        
        power = 1
        while leftover * 10**power < divnum:
            power += 1
        divds[leftover] = (leftover * 10**power % divnum,power)
        leftover=leftover * 10**power % divnum
        #print(divds)
        #print(leftover)
        if divds[leftover] != (0,0):
            cycleStart = leftover
            break
        

    if cycleStart == 0:
        return count
    
    curr = divds[cycleStart][0]
    count+=divds[cycleStart][1]
    while curr != cycleStart:
        count += divds[curr][1]
        curr = divds[curr][0]
        
    

    return count

maxval=0
maxnum=0
for i in range(2,1000):
    print(i)
    n = find(i)
    if n > maxval:
        maxnum = i
        maxval = n
        

