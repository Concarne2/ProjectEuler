def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

factorials=[1]
for i in range(1,10):
    factorials.append(factorial(i))

def nextnum(n):
    total = 0
    for s in str(n):
        total += factorials[int(s)]
    return total



loopers=[1,2,145,169,363601,1454,871,45361,872,45362]

asdf = 0
for n in range(3,1000000):
    count = 0
    if(n == nextnum(n)):
        continue
    nums = n
    
    while nums not in loopers:
        nums = nextnum(nums)
        count+=1
        if(nums == nextnum(nums)):
            break
    if nums == 169 or nums== 363601 or nums==1454:
        count += 3
    elif nums == 871 or nums == 45361 or nums == 872 or nums == 45362:
        count+=2
    if(count >= 60):
        print(n)
        asdf += 1
print(asdf)
