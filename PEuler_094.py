x=0
y=0

def do1():
    global x
    global y
    newx = -2*x-y-2
    newy = -3*x-2*y-2
    x=newx
    y=newy

def do2():
    global x
    global y
    newx = -2*x-y-1
    newy = -3*x-2*y-1
    x=newx
    y=newy

x=0
y=1
total=0
while True:
    do1()
    do1()
    if 6*x+2>1000000000:
        break
    print((x,y))
    total+=6*x+2
    

x=0
y=0
while True:
    do2()
    do2()
    if 6*x+4>1000000000:
        break
    
    total+=6*x+4
    print((x,y))
    
print(total)
