import time
'''
def IsBouncys(n):
    inc = -1
    #0 is increasing, 1 is decreasing, 2 is bouncy
    ns = str(n)
    start = 0
    while ns[start] == ns[start+1]:
        start+=1
        if start == len(ns) - 1:
            return False
    if int(ns[start]) < int(ns[start + 1]):
        inc = 0
    else:
        inc = 1
    if inc == 0:
        for i in range(start+1,len(ns)-1):
            if int(ns[i]) > int(ns[i+1]):
                return True
    elif inc == 1:
        for i in range(start+1,len(ns)-1):
            if int(ns[i]) < int(ns[i+1]):
                return True
            
    return False  
'''

def IsNotBouncy(num):
    n=num
    if n<10:
        return True
    inc = -1
    #0 is increasing, 1 is decreasing, 2 is bouncy
    ns=[]
    while n>=10:
        ns.append(n%10)
        n = n//10
    ns.append(n)
    ns.reverse()
    start = 0
    while ns[start] == ns[start+1]:
        start+=1
        if start == len(ns) - 1:
            return True
    if ns[start] < (ns[start + 1]):
        inc = 0
    else:
        inc = 1
        

    if inc == 0:
        for i in range(start+1,len(ns)-1):
            if (ns[i]) > (ns[i+1]):
                return False
        return True
    
    elif inc == 1:
        for i in range(start+1,len(ns)-1):
            if (ns[i]) < (ns[i+1]):
                return False
        return False

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

#n자리: 9Hn+(10Hn-1)-9    

nbc = 0
nbc += 9

for n in range(2,101):
    nbc += int(fact(9+n-1)/fact(n)/fact(9-1))
    nbc += int(fact(10+n-1)/fact(n)/fact(10-1)) - 1
    nbc -=9
print(nbc)

'''
nonbouncyCount = 0
n=10
while n<100:
    if IsNotBouncy(n):
        nonbouncyCount+=1
        print(n)
    n+=1
    #12952
    #4954
print(nonbouncyCount)
'''
