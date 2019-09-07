fib=[]
fib.append(1)
fib.append(1)
while len(str(fib[len(fib)-1]))<1000:
    fib.append(fib[len(fib)-1]+fib[len(fib)-2])
