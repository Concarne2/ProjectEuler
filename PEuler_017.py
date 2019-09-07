dic = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:7,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,1000:11}



def calc(n):
    if n in dic:
        return dic[n]

    if n<100:
        tens = n // 10
        return dic[tens*10] + dic[n - tens*10]

    hundreds = n // 100
    return dic[hundreds] + 7 + 3 + calc(n - hundreds*100)
        
val=0
for i in range(1,1001):
	val += calc(i)
