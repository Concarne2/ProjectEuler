import math

def swap(A,i,j):
    temp = A[i]
    A[i]=A[j]
    A[j] = temp

def generate(n,A,word1,word2):
    if n==1:
        tryWithThis(A,word1,word2)
    else:
        for i in range(0,n-1):
            generate(n-1,A,word1,word2)
            if n%2==0:
                swap(A,i,n-1)
            else:
                swap(A,0,n-1)
        generate(n-1,A,word1,word2)


f = open("p098_words.txt","r")
words = f.read().replace('"','').split(",")
f.close()

maxlen=0
for word in words:
    if len(word)>maxlen:
        maxlen=len(word)

wordsbylen=[]

for i in range(0,maxlen+1):
    wordsbylen.append([])

def isanag(word1,word2):
    pool1=[]
    pool2=[]
    for i in range(0,26):
        pool1.append(0)
        pool2.append(0)
    for w in word1:
        pool1[ord(w)-65]+=1
    for w in word2:
        pool2[ord(w)-65]+=1
    return pool1==pool2

for word in words:
    alone=True
    for anags in wordsbylen[len(word)]:
        if isanag(anags[0],word):
            anags.append(word)
            alone=False
            break
    if alone:
        wordsbylen[len(word)].append([word])

longest = 0

for wordpool in wordsbylen:
    for words in wordpool:
        if len(words)>=2:
            longest = max(longest,len(words[0]))
            print(words)
           
words1=[]
words2=[]

for words in wordsbylen[5]:
    if len(words)>=2:
        words1.append(words[0])
        words2.append(words[1])


cantend=[2,3,7,8]
results1=[]
results2=[]

def isSqrt(n):
    c = math.sqrt(n)
    return c == int(c)

def tryWithThis(A,word1,word2):
    keys={}
    if A[0]==0 or A[len(word1)-1] in cantend:
        return
    numstr1 = ''
    for n in A[:len(word1)]:
        numstr1 = numstr1+str(n)
    if not isSqrt(int(numstr1)):
        return
    
    for i in range(0,len(word1)):
        keys[word1[i]]=A[i]
    numstr2=''
    for c in word2:
        numstr2 = numstr2 + str(keys[c])
    if numstr2[0] == '0' or numstr2[len(word1)-1] in cantend:
        return
    if not isSqrt(int(numstr2)):
        return
    results1.append(numstr1)
    results2.append(numstr2)

for i in range(0,len(words1)):
    print(words1[i])
    numbers=[0,1,2,3,4,5,6,7,8,9]
    generate(10,numbers,words1[i],words2[i])


