results = [0,0,1,2]

def nextResult():
    n = len(results)
    ways = results[n-1] + 1
    for i in range(2,n//2 + 1):
        ways += results[n//i]
    results.append(ways)
        
    
ways = [1]

for i in range(1,101):
    ways.append(0)

for i in range(1,100):
    for j in range(i,101):
        ways[j] += ways[j-i]
        
