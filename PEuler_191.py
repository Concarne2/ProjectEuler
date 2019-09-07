dic={}
dic['A0'] = 1
dic['A1'] = 1
dic['A2'] = 0
dic['A0L'] = 1
dic['A1L'] = 0
dic['A2L'] = 0

def next():
    A0= dic['A0']
    A1 = dic['A1']
    A2 = dic['A2']
    A0L = dic['A0L']
    A1L = dic['A1L']
    A2L = dic['A2L']
    dic['A0'] = A0 + A1 + A2
    dic['A1'] = A0
    dic['A2'] = A1
    dic['A0L'] = A0 + A1 + A2 + A0L + A1L + A2L 
    dic['A1L'] = A0L
    dic['A2L'] = A1L
    print(sum(dic.values()))
for i in range(1,30):
    next()
