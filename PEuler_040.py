num = 1
count = 1

total=1
power = 1

while count <= 1000000:
    num+=1
    numstr = str(num)
    for n in numstr:
        count += 1
        if count % (10**power) == 0:
            total *= int(n)
            print(n)
            power += 1
