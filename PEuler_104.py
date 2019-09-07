contains=[]
for i in range(0,10):
    contains.append(False)
def ispan(n):
    for dig in n:
        if int(dig) == 0:
            for i in range(0,10):
                contains[i] = False
            return False
        if contains[int(dig)]:
            for i in range(0,10):
                contains[i] = False
            return False
        contains[int(dig)] = True

    for i in range(0,10):
        contains[i] = False
        
    return True

fib1=1
fib2=1

for i in range(3,100):
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp

for i in range(100,1000000):
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    '''
    if ispan(str(fib2)[:9]):
       # if ispan(str(fib2)[-9:]):
        print(i)
'''
