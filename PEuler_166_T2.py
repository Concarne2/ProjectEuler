import numpy as np
from scipy.linalg import lu



equations = np.array([[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
                [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],
                [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
                [0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]])

#8 10 11 12 14 15 16 are free variables

equ_cut = np.array(equations[:,[0,1,2,3,4,5,6,8,12]]).reshape(9,9)

equ_inverse = np.linalg.inv(equ_cut)
'''
equ_cut =
array([[1, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 1, 0, 0, 1, 1],
       [0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 1]])


#sol = np.array([6,3,3,0,5,0,4,0,1])
sums = np.array([12,  9,  3,  3, 12,  6,  6,  6,  9])
sol = np.matmul(equ_inverse,sums)
'''

count = 0
sum_val = 0
for sum_val in range(0,37):
    print(sum_val)
    for num_8 in range(max(0,sum_val - 27),min(10,sum_val+1)):
        for num_12 in range(max(0,sum_val - 27-num_8),min(10,sum_val+1-num_8)):
            for num_11 in range(max(0,sum_val - 27-num_12),min(10,sum_val+1-num_12)):
                for num_10 in range(0,min(10,sum_val+1-num_12-num_11)):
                    for num_14 in range(0,min(10,sum_val+1-num_10)):
                        for num_15 in range(0,min(10,sum_val+1 - num_14, sum_val+1-num_11)):
                            for num_16 in range(0,min(10,sum_val+1-num_8-num_12,sum_val+1-num_11)):
                                totalSums = np.array([sum_val, sum_val-num_8, sum_val-num_10-num_11-num_12, sum_val-num_14-num_15-num_16, sum_val, sum_val-num_10-num_14, sum_val-num_11-num_15, sum_val-num_11-num_16, sum_val-num_10])

                                isThisGood = True
                                sol= np.matmul(equ_inverse,totalSums)
                                for n in sol:
                                    if (not n.is_integer()) or n < 0 or n > 9:
                                        isThisGood = False
                                        break
                                if isThisGood:
                                    '''
                                    solution = np.zeros((4,4))
                                    solution[0] = sol[:4]
                                    solution[1][0]=sol[4]
                                    solution[1][1]=sol[5]
                                    solution[1][2]=sol[6]
                                    solution[1][3]=num_8
                                    solution[2][0]=sol[7]
                                    solution[2][1]=num_10
                                    solution[2][2]=num_11
                                    solution[2][3]=num_12
                                    solution[3][0]=sol[8]
                                    solution[3][1]=num_14
                                    solution[3][2]=num_15
                                    solution[3][3]=num_16
                                    print(solution)
                                    '''
                                    count+=1
                                       

print(count)
'''
sum_val = 36
num_8 = 9
num_10=9
num_11=9
num_12=9
num_14=9
num_15=9
num_16=9
asdf = [sum_val, sum_val-num_8, sum_val-num_10-num_11-num_12, sum_val-num_14-num_15-num_16, sum_val, sum_val-num_10-num_14, sum_val-num_11-num_15, sum_val-num_11-num_16, sum_val-num_10]
print(np.matmul(equ_cut,np.array([9,9,9,9,9,9,9,9,9])))
print(asdf)
fdsa = np.matmul(equ_inverse,asdf)
'''
