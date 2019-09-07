def cancel(num,den):
    if num == den:
        return (0,0)
    numstr=str(num)
    denstr=str(den)
    if numstr[0]==denstr[1] and numstr[1]==denstr[0]:
        return (0,0)
    for n in range(0,2):
        for d in range(0,2):
            if numstr[n] == denstr[d]:
                newnum = int(numstr[1-n])
                newden = int(denstr[1-d])
                return (newnum,newden)
    return (0,0)

results=[]
for den in range(11,99):
    for num in range(10,den):
        if den % 10 == 0 and num % 10 == 0:
            continue
        result = cancel(num,den)
#        print(result)
#        print(str(num)+" "+str(den))
        if result[1]!=0:
            if num/den == result[0]/result[1]:
                results.append(result)
