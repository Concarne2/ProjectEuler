op = 2

num = 600851475143

while op < num:
    if(num % op == 0):
        num = num/op
        op=2
        continue
    op +=1

print(op)
