fib1 = 1

fib2 = 1

result=0

while fib2 <= 4000000:
    if(fib2 % 2 == 0):
        result+=fib2
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp

print(result)
