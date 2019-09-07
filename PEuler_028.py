current=1
total=0
count=0
addAmount=2

while current <= 1001*1001:
    total += current
    current += addAmount
    count += 1
    if count == 4:
        count = 0
        addAmount+=2
