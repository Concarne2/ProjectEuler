import numpy as np

#N = 100, N = 2n
n = 50

mat = np.zeros((n,n))

mat[0][0] = -17/36
mat[0][1] = 2/9
mat[0][2] = 1/36


mat[1][0] = 2/9
mat[1][1] = -1/2
mat[1][2] = 2/9
mat[1][3] = 1/36

for k in range(2,n-2):
    mat[k][k-2] = 1/36
    mat[k][k-1] = 2/9
    mat[k][k] = -1/2
    mat[k][k+1] = 2/9
    mat[k][k+2] = 1/36

mat[-2][-4] = 1/36 
mat[-2][-3] = 2/9
mat[-2][-2] = -17/36
mat[-2][-1] = 2/9

mat[-1][-3] = 1/18
mat[-1][-2] = 4/9
mat[-1][-1] = -1/2

res = np.zeros(n) - 1

sol = np.linalg.solve(mat,res)

print(sol[-1])
