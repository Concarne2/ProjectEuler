'''
3 one
3 two
5 three
4 four
4 five
3 six
5 seven
5 eight
4 nine
3 ten
6 eleven
6 twelve
8 thirteen
8 fourteen
7 fifteen
7 sixteen
9 seventeen
8 eighteen
8 nineteen
6 twenty
6 thirty
5 forty
5 fifty
5 sixty
7 seventy
6 eighty
6 ninety
'''

dic = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,1000:11}

def calc(n):
    if n in dic:
        return dic[n]

    if n<100:
        tens = n // 10
        return dic[tens*10] + dic[n - tens*10]

    if n%100 == 0:
        return dic[n/100] + 7
    hundreds = n // 100
    return dic[hundreds] + 7 + 3 + calc(n - hundreds*100)
        
val=0
for i in range(1,1001):
	val += calc(i)
	print(val)

