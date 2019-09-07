def isPalind(n):
    for i in range(1,len(n)):
        if n[i] != n[-i-1]:
            return False

    return True

def isLychrel(n,tries):
    if tries > 50:
        return True
    added = n + int(str(n)[::-1])
    if isPalind(str(added)):
        return False
    else:
        return isLychrel(added,tries + 1)

count = 0
for i in range(10,10000):
    if isLychrel(i,1):
        print(i)
        count += 1
print(count)
