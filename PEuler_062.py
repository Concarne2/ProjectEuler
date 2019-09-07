
def newDigits():
    digits=[0,0,0,0,0,0,0,0,0,0]
    return digits
def findDigits(n):
    digits = newDigits()
    strn = str(n)
    for c in strn:
        digits[int(c)] += 1
    return digits

currlen = 0
permutations={}

for num in range(100,10000):
    
    cube = num * num * num
    if len(str(cube)) > currlen:
        currlen = len(str(cube))
        permutations = {}
    digits = findDigits(cube)
    if str(digits) in permutations:
        permutations[str(digits)][0] += 1
        permutations[str(digits)].append(num)
        if(permutations[str(digits)][0] > 4):
            print(str(digits))
            print(permutations[str(digits)])
    else:
        permutations[str(digits)] = [1]
        permutations[str(digits)].append(num)
    
