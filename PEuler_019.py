year = 1900
day=1
count=0

def do(n):
    global day
    global count
    day+=n
    day = day%7
    if day==0:
        count+=1

while year<2000:
    do(31)
    if year%4 == 0:
        if year==1900:
            do(28)
        else:
            do(29)
    else:
        do(28)
    do(31)
    do(30)
    do(31)
    do(30)
    do(31)
    do(31)
    do(30)
    do(31)
    do(30)
    do(31)
    year+=1
print(count)
