def tobin(n):
    text=""
    while n>=1:
        if n%2==1:
            text="1"+text
        else:
            text="0"+text
        n=n//2
    return text

def checkpal(n):
    for i in range(0,len(n)//2):
        if n[i] != n[len(n)-1-i]:
            return False
    return True

val=0
for n in range(1,1000000):
    if checkpal(str(n)):
        if checkpal(tobin(n)):
            val+=n
print(val)
