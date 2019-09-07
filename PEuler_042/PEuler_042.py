trys=[]

for i in range(0,440):
    trys.append(False)

for n in range(1,30):
    trys[(int(n*(n+1)/2))]=True


def findval(s):
    total=0
    for a in s:
        total+=(ord(a)-64)
    return total

f = open("p042_words.txt","r")

totalstr=f.read()
f.close()

replaced=totalstr.replace('"',"")

words=replaced.split(",")

count=0
for w in words:
    if trys[findval(w)]:
        count+=1

print(count)
