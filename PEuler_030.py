
def check(n):
    numstr=str(n)
    numlist=[]
    for s in numstr:
        numlist.append(int(s))
    val = 0
    for num in numlist:
        val += num ** 5
    if val == n:
        return True
    else:
        return False

val=0

for n in range(10,(9**5)*6+1):
    if check(n):
        print(n)
        val+=n
print(val)
