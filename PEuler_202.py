from math import gcd as bltin_gcd

def coprime(a, b):
    return bltin_gcd(a, b) == 1

'''
a = 499997
b = 5
'''

n = 12017639147

a = int((n + 3)/2) - 2
b = 2

print(a)
count = 0

while a > b:
    if coprime(a,b):
        count +=1
    a-=3
    b+=3

print(count)
