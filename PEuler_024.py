factorials=[]

val=1
for i in range(1,11):
    val *= i
    factorials.append(val)

million=1000000
summation=0
addedAmount=[]
for i in range(0,len(factorials)):
    count = 0
    while million - summation >= factorials[len(factorials)-1-i]:
        summation += factorials[len(factorials)-1-i]
        count+=1
    addedAmount.append(count)
        
print(addedAmount)
