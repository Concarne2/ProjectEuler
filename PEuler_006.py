squareSum = 0

sumResult = 0
sumSquare = 0

for i in range(1,101):
    squareSum += i * i
    sumResult += i
sumSquare = sumResult * sumResult

print(sumSquare - squareSum)
