pents=[1,5,12,22,35]

def expand():
    n = len(pents) + 1
    pents.append(int(n*(3*n-1)/2))

stopper = True
curridx=2
while stopper:
    if curridx == len(pents):
        expand()
    for j in range(0,curridx):
        pk = pents[curridx]
        pj = pents[j]
        if pk - pj in pents:
            #print(str(pk)+" - "+str(pj))
            while pents[-1] < pk + pj:
                expand()
            if pk + pj in pents:
                print(str(pk)+" + "+str(pj))
                stopper = False
    curridx += 1
    #print(str(curridx)+", "+str(len(pents)))
