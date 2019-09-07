def calc(n):
    n = n * 2
    if len(str(n)) > 10:
        n = int(str(n)[-10:])
    return n

n = 1

for k in range(0,7830457):
    n = calc(n)
