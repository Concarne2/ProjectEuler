'''
def isPrime(num):
    for i in range(3,num):
        if(num % i == 0):
            return False
    return True

count = 1
num = 3

while count< 10001:
    if isPrime(num):
        count += 1
    num += 2

print(num)
'''

def is_Prime(x):
	y = 2
	while y**2 <= x:
		if x % y == 0:
			return 0
		y += 1
	
	return 1

q = 1
p = 0

while p < 10000:
	if is_Prime(q) == 1:
		print(q)
		p += 1
	q += 2

print(q)
