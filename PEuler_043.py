currnums=[]
nextnums=[]

currnums.append("1")
for n in range(2,10):
    nextnums=[]
    for c in currnums:
        for i in range(0,len(c)+1):
            nextnums.append(c[:i]+str(n)+c[i:])
    currnums=nextnums[:]

nextnums=[]
for c in currnums:
    for i in range(1,len(c)+1):
        nextnums.append(c[:i]+str(0)+c[i:])
val=0
for num in nextnums:
    if int(num[-3:]) % 17 == 0:
        if int(num[-4:-1]) % 13 == 0:
            if int(num[-5:-2]) % 11 == 0:
                if int(num[-6:-3]) % 7 == 0:
                    if int(num[-7:-4]) % 5 == 0:
                        if int(num[-8:-5]) % 3 == 0:
                            if int(num[-9:-6]) % 2 == 0:
                                val+=int(num)
                                print(num)
                
print(val)
