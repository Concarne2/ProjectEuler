ab = [3,2]

def forward(ab):
    a = ab[0]
    b = ab[1]
    ab[0] = 2*b + a
    ab[1] = b + a


count = 0

for i in range(1,1000):
    forward(ab)
    if len(str(ab[0])) > len(str(ab[1])):
        count += 1
print(count)
