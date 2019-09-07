f = open("p079_keylog.txt","r")
data = f.read()

keys = data.split()

keylist = [0,1,2,3,4,5,6,7,8,9]
'''
index -> the number
number on the index -> order
'''
def swap(a,b):
    temp = keylist[a]
    keylist[a] = keylist[b]
    keylist[b] = temp

for keystr in keys:
    first = int(keystr[0])
    second = int(keystr[1])
    third = int(keystr[2])
    if keylist[first] > keylist[second]:
        swap(first,second)
    if keylist[second] > keylist[third]:
        swap(second,third)
    if keylist[first] > keylist[second]:
        swap(first,second)
answer=''
for i in range(0,10):
    num = keylist.index(i)
    if not num == i:
        answer += str(num)
