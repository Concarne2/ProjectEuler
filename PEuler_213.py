import numpy as np

DIM = 5

w = np.zeros((DIM**2,DIM**2))


for i in range(1,(DIM - 1)):
    for j in range(1,(DIM - 1)):
        w[DIM*i+j][DIM*(i+1)+j] = 0.25
        w[DIM*i+j][DIM*(i-1)+j] = 0.25
        w[DIM*i+j][DIM*i+j+1] = 0.25
        w[DIM*i+j][DIM*i+j-1] = 0.25


for j in range(1,(DIM - 1)):
    w[DIM*1+j][j] = 1/3
    w[DIM*(DIM - 2)+j][DIM*(DIM - 1)+j] = 1/3

    w[j][j-1] = 1/3
    w[j][j+1] = 1/3
    w[j][j+DIM] = 1/4
    w[DIM*(DIM - 1)+j][DIM*(DIM - 1)+j-1] = 1/3
    w[DIM*(DIM - 1)+j][DIM*(DIM - 1)+j+1] = 1/3
    w[DIM*(DIM - 1)+j][DIM*(DIM - 1)+j-DIM] = 1/4

for i in range(1,(DIM - 1)):
    w[DIM*i+1][DIM*i] = 1/3
    w[DIM*i+(DIM - 2)][DIM*i+(DIM - 1)] = 1/3
    
    w[DIM*i][DIM*(i-1)] = 1/3
    w[DIM*i][DIM*i+1] = 1/4
    w[DIM*i][DIM*(i+1)] = 1/3
    w[DIM*i+(DIM - 1)][DIM*(i-1)+(DIM - 1)] = 1/3
    w[DIM*i+(DIM - 1)][DIM*i+(DIM - 1)-1] = 1/4
    w[DIM*i+(DIM - 1)][DIM*(i+1)+(DIM - 1)] = 1/3


w[0][1] = 1/3
w[0][DIM] = 1/3
w[(DIM - 1)][(DIM - 2)] = 1/3
w[(DIM - 1)][2*DIM-1] = 1/3
w[DIM*(DIM - 1)][DIM*(DIM - 1)+1] = 1/3
w[DIM*(DIM - 1)][DIM*(DIM - 2)] = 1/3
w[DIM*(DIM - 1)+(DIM - 1)][DIM*(DIM - 1)+(DIM - 2)] = 1/3
w[DIM*(DIM - 1)+(DIM - 1)][DIM*(DIM - 2)+(DIM - 1)] = 1/3

w[1][0] = 1/2
w[DIM][0] = 1/2
w[(DIM - 2)][(DIM - 1)] = 1/2
w[(DIM - 1)+DIM][(DIM - 1)] = 1/2
w[DIM*(DIM - 2)][DIM*(DIM - 1)] = 1/2
w[DIM*(DIM - 1)+1][DIM*(DIM - 1)] = 1/2
w[DIM*(DIM - 1)+(DIM - 1)-1][DIM*(DIM - 1)+(DIM - 1)] = 1/2
w[DIM*(DIM - 2)+(DIM - 1)][DIM*(DIM - 1)+(DIM - 1)] = 1/2



res = np.zeros(DIM**2)+1

for i in range(49):
    res = np.matmul(w,res)

probs = np.

'''
expect = 0
for i in range(DIM**2):
    prob = 1
    jumps = res*w[i]
    for p in jumps[jumps!=0]:
        prob *= (1-p)
    expect += prob
print(expect)
'''
