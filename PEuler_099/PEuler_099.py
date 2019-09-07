import numpy as np

f = open("p099_base_exp.txt",'r')
lines = f.readlines()
f.close()


bottom=[]
power=[]

for line in lines:
    bottom.append(int(line.strip().split(',')[0]))
    power.append(int(line.strip().split(',')[1]))

maxim=0
linecount=0
for i in range(0,len(bottom)):
    num = np.log(bottom[i]) * power[i]
    if num > maxim:
        maxim=num
        linecount=i+1
print(linecount)
