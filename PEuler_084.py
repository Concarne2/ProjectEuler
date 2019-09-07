import numpy as np

G2J = 30

JAIL = 10

CC = [2, 17, 33]

CH = [7, 22, 36]

R = [5, 15, 25, 35]
U = [12, 28]

def nextR(n):
    if n < 5 or n > 35:
        return 5
    elif n<15:
        return 15
    elif n<25:
        return 25
    else:
        return 35

def nextU(n):
    if n>12 and n<28:
        return 28
    else:
        return 12

#doubleRoll = [1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
doubleRoll = [1/16,2/16,3/16,4/16,3/16,2/16,1/16]

chanceCalc = np.zeros((40,40))

for i in range(0,40):
    chanceCalc[i][range(i-len(doubleRoll) - 1,i-1)] += doubleRoll

######### Go To Jail #########
chanceCalc[G2J] = 0
chanceCalc[G2J][G2J]=1
chanceCalc[JAIL][range(G2J-len(doubleRoll) - 1,G2J-1)] += doubleRoll
##############################


chanceCalc[:,CC] *= 7/8

chanceCalc[:,CH] *= 3/8

chanceCalc[0,CC] += 1/16

chanceCalc[JAIL,CC] += 1/16

for i in [0,JAIL,11,24,39,5]:
    chanceCalc[i,CH] += 1/16

for ch in CH:
    chanceCalc[nextR(ch),ch] += 1/8
    chanceCalc[nextU(ch),ch] += 1/16
    chanceCalc[ch-3,ch]+=1/16


#chanceCalc[:,G2J] = 0



for i in range(0,40):
    chanceCalc[i][i] = -1


chanceCalc[1] = 1

sol = np.zeros(40)
sol[1] = 1
solution = np.linalg.solve(chanceCalc,sol)
print(solution)

