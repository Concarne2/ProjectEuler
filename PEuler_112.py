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

def IsBouncy(n):
    if n<10:
        return False
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
            return False
    if ns[start] < (ns[start + 1]):
        inc = 0
    else:
        inc = 1
        

    if inc == 0:
        for i in range(start+1,len(ns)-1):
            if (ns[i]) > (ns[i+1]):
                return True
    '''
    elif inc == 1:
        for i in range(start+1,len(ns)-1):
            if (ns[i]) < (ns[i+1]):
                return True
    '''
    return False 

nonbouncyCount = 0
n=100
while n<=1000:
    if not IsBouncy(n):
        nonbouncyCount+=1
        print(n)
    n+=1
    '''
    if (n%100 == 0 and bouncyCount == n-int((n/100))):
        print(n)
        break
    n+=1
    if n%1000==0:
        print(n)'''
    #12952
    #4954

print(nonbouncyCount)
