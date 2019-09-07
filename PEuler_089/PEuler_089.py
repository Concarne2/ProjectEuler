f = open("p089_roman.txt","r")
numerals = f.read().split("\n")
f.close()

roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

saved=0

for numeral in numerals:
    
    original = len(numeral)
    trimmed=0
    changed=''
    n = 0
    for i in range(0,len(numeral)-1):
        if roman[numeral[i]] == 1 or roman[numeral[i]]==10 or roman[numeral[i]]==100:
            if roman[numeral[i+1]] == 5*roman[numeral[i]] or roman[numeral[i+1]] == 10*roman[numeral[i]]:
                n-=2*roman[numeral[i]]
        n+= roman[numeral[i]]
    n+=roman[numeral[-1]]
    '''
    print(numeral)
    print(n)
    print(original)'''
    
    while n>=1000:
        n-=1000
        trimmed+=1
        changed=changed+'M'
    if n>=900:
        n-=900
        trimmed+=2
        changed=changed+'CM'
        '''
    if n>=800:
        n-=800
        trimmed+=3
        '''
    elif n>=500:
        n-=500
        trimmed+=1
        changed=changed+'D'
    elif n>=400:
        n-=400
        trimmed+=2
        changed=changed+'CD'
    while n>=100:
        n-=100
        trimmed+=1
        changed=changed+'C'
    if n>=90:
        n-=90
        trimmed+=2
        changed=changed+'XC'
        '''
    if n>=80:
        n-=80
        trimmed+=3
        '''
    elif n>=50:
        n-=50
        trimmed+=1
        changed=changed+'L'
    elif n>=40:
        n-=40
        trimmed+=2
        changed=changed+'XL'
    while n>=10:
        n-=10
        trimmed+=1
        changed=changed+'X'
    if n>=9:
        n-=9
        trimmed+=2
        changed=changed+'IX'
        '''
    if n>=8:
        n-=8
        trimmed+=3
        '''
    elif n>=5:
        n-=5
        trimmed+=1
        changed=changed+'V'
    elif n>=4:
        n-=4
        trimmed+=2
        changed=changed+'IV'
    while n>=1:
        n-=1
        trimmed+=1
        changed=changed+'I'
        '''
    print(changed)
    print(trimmed)'''
    saved += original - len(changed)
print(saved)
