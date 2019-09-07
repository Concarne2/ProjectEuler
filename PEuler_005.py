#brute force
'''
num=21
tryer = True

while num<200000000:
    tryer = True
    num+=1
    for i in range(2,20):
        if num % i != 0:
            tryer = False
    print(num)
    if tryer:
        break
print (num)
'''

num = 20
total = 1

def isPrime(num):
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

for i in range(2,num+1):
    if isPrime(i):
        multer = i
        while multer <= num:
            total *= i
            multer *=i

print(total)
        
