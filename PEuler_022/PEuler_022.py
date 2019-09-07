f = open("names.txt", "r")
nameStr = f.read()
f.close()

nameStr=nameStr.replace('"',"")
names=nameStr.split(",")
names.sort()
score=0
for i in range(0,len(names)):
    value=0
    for letter in names[i]:
        value+=(ord(letter)-64)
    score+=(value*(i+1))
print(score)
