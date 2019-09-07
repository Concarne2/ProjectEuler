
#total nums to be multiplied, current pos, Array
'''
def do(t, c, A):
    if t == c:
        A[c] = current
        print(A[:t+1])
        for A[c+1:]:
'''

#total number count, current pos, num on current pos, total nums to be multiplied, num to be added
#currpos starts from 1, 0 is used to initiate the algorithm
def do(total, currpos, currnum, mult, multipliednum, totals):
    if currpos == mult:
        totals[0] += multipliednum * currnum
    elif currpos == 0:
        for n in range(1, total - mult + 2):
            do(total, 1, n, mult, 1, totals)
    else:
        for n in range(currnum+1, total - mult + 2 + currpos):
            do(total, currpos + 1, n, mult, multipliednum * currnum, totals)

def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n

tot = [1]
MAX = 15

for m in range(1,MAX//2+1):
    do(MAX,0,0,m,0,tot)

prob = tot[0] / fact(MAX+1)


money = fact(MAX+1) // tot[0]
print(money)
