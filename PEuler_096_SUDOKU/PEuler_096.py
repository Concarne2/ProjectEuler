grids=[]
import time
class grid:
    def __init__(self,d):
        self.data=[]
        self.candidates=[]
        self.zeros=[]
        self.numOfZeros=0
        for i in range(1,len(d)-1):
            thisrow=[]
            for c in d[i]:
                thisrow.append(int(c))
            self.data.append(thisrow)
        for i in range(0,9):
            candidaterow=[]
            for j in range(0,9):
                candidaterow.append([])
            self.candidates.append(candidaterow)
        '''
        for i in range(0,len(self.rows[0])):
            col = ''
            for j in range(0,len(self.rows)):
                col = col + self.rows[j][i]
            self.cols.append(col)
        for i in range(0,3):
            for j in range(0,3):
                s = ''
                for n in range(0,3):
                    for m in range(0,3):
                        s = s + self.rows[3*i+n][3*j+m]
                self.areas.append(s)
        '''
    def backup(self):
        backupDat=[]
        for line in self.data:
            backupDat.append(line.copy())
        return backupDat
    def row(self,n):
        r = ''
        for num in self.data[n]:
            r = r + str(num)
        return r
    def col(self,n):
        c = ''
        for row in self.data:
            c = c + str(row[n])
        return c
    def area(self,n):
        i=0
        j=0
        a=''
        while n>=3:
            n-=3
            i+=1
        while n>0:
            n-=1
            j+=1
        for n in range(0,3):
            for m in range(0,3):
                a = a + str(self.data[3*i+n][3*j+m])
        return a
    def updateCandidate(self,r,c):
        rowcandid = missing(self.row(r))
        colcandid = missing(self.col(c))
        areacandid= missing(self.area(3*(r//3)+(c//3)))
        count=0
        candid=[]
        for n in rowcandid:
            if n in colcandid and n in areacandid:
                candid.append(n)
                count+=1
        self.candidates[r][c] = candid
        return count

    def updateCandidate2(self,r,c):
        count=0
        candid=[]
        for n in range(1,10):
            if not self.inRow(r,n):
                if not self.inCol(c,n):
                    if not self.inArea(3*(r//3)+(c//3),n):
                        candid.append(n)
                        count+=1
        self.candidates[r][c] = candid
        return count

    def inRow(self,row,num):
        return num in self.data[row]
    
    def inCol(self,col,num):
        for i in range(0,9):
            if num == self.data[i][col]:
                return True
        
        return False
    
    def inArea(self,area,num):
        for i in range(0,3):
            for j in range(0,3):
                if num==self.data[3*(area//3)+i][3*(area%3)+j]:
                    return True
        return False
    
    def isPossible(self,r,c,num):
        ns= str(num)
        if ns in self.row(r):
            return False
        if ns in self.col(c):
            return False
        if ns in self.area(3*(r//3)+(c//3)):
            return False
        return True

    def missingLocation(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.data[i][j]==0:
                    return (i,j)
        return(9,9)

    
    def missingLocation2(self):
        least=100
        self.updateZeros2()
        least0s=min(self.zeros)
        for i in range(0,9):
            for j in range(0,9):
                if self.data[i][j]==0:
                    l = self.updateCandidate2(i,j)
                    if l<least:
                        least=l


        for i in range(0,9):
            if g.zeros[i]==least0s:
                for j in range(0,9):
                    if self.data[i][j]==0:
                        if len(self.candidates[i][j])==least:
                            return (i,j)

        for j in range(0,9):
            if g.zeros[9+j]==least0s:
                for i in range(0,9):
                    if self.data[i][j]==0:
                        if len(self.candidates[i][j])==least:
                            return (i,j)

        for a in range(0,9):
            if g.zeros[18+a]==least0s:
                for i in range(3*(a//3),3*(a//3)+3):
                    for j in range(3*(a%3),3*(a%3)+3):
                        if self.data[i][j]==0:
                            if len(self.candidates[i][j])==least:
                                return (i,j)
                            
        for i in range(0,9):
            for j in range(0,9):
                if self.data[i][j]==0:
                    if len(self.candidates[i][j])==least:
                        return (i,j)
        
        return(9,9)
                    
    

    def updateZeros(self):
        count=0
        
        '''self.zeros=[]
        for i in range(0,9):
            z = countzeros(self.row(i))
            count += z
            self.zeros.append(z)
            
        self.numOfZeros = count

        for i in range(0,9):
            self.zeros.append(countzeros(self.col(i)))
        for i in range(0,9):
            self.zeros.append(countzeros(self.area(i)))
            '''
        for i in range(0,9):
            for j in range(0,9):
                if self.data[i][j]==0:
                    count+=1
        self.numOfZeros = count
        
    def updateZeros2(self):
        self.zeros=[]
        for i in range(0,9):
            z=0
            for j in range(0,9):
                if g.data[i][j]==0:
                    z+=1
            self.zeros.append(z)
        for i in range(0,9):
            z=0
            for j in range(0,9):
                if g.data[j][i]==0:
                    z+=1
            self.zeros.append(z)
        for a in range(0,9):
            z=0
            for i in range(0,3):
                for j in range(0,3):
                    if 0==self.data[3*(a//3)+i][3*(a%3)+j]:
                        z+=1
            self.zeros.append(z)
        
def countzeros(s):
    count = 0
    for c in s:
        if c=='0':
            count+=1
    return count


def missing(s):
    for i in range(0,100):
        miss=[]
        for n in range(1,10):
            if str(n) not in s:
                miss.append(n)
    return miss
    
def tryThis(g):
    g.updateZeros()
    '''print (g.zeros)'''
    if g.numOfZeros==0:
        print("solved")
        return False
    
    
    '''

    for i in range(0,9):
        if g.zeros[i]==least0s:
            for j in range(0,9):
                if g.data[i][j]==0:
                    if g.updateCandidate(i,j)==1:
                        g.data[i][j]=g.candidates[i][j][0]
                        return True
                    elif len(g.candidates[i][j])==0:
                        return False

    for j in range(0,9):
        if g.zeros[9+j]==least0s:
            for i in range(0,9):
                if g.data[i][j]==0:
                    if g.updateCandidate(i,j)==1:
                        g.data[i][j]=g.candidates[i][j][0]
                        return True
                    elif len(g.candidates[i][j])==0:
                        return False

    for a in range(0,9):
        if g.zeros[18+a]==least0s:
            for i in range(3*(a//3),3*(a//3)+3):
                for j in range(3*(a%3),3*(a%3)+3):
                    if g.data[i][j]==0:
                        if g.updateCandidate(i,j)==1:
                            g.data[i][j]=g.candidates[i][j][0]
                            return True
                        elif len(g.candidates[i][j])==0:
                            return False
    '''

    '''
    leastCandids=100

    
    for i in range(0,9):
        for j in range(0,9):
            if g.data[i][j]==0:
                l = g.updateCandidate(i,j)
                '''
    '''
                if l==0:
                    return False
                elif l==1:
                    g.data[i][j] = g.candidates[i][j][0]
                elif l<leastCandids:
                    leastCandids=l'''
    ''' "might help with efficiency"
    least0s = 10
    for z in g.zeros:
        if z!=0 and z<least0s:
            least0s = z'''

    '''
    for i in range(0,9):
        if g.zeros[i]==least0s:
            for j in range(0,9):
                if g.data[i][j]==0 and len(g.candidates[i][j])==leastCandids:
                    for cand in g.candidates[i][j]:
                        backupData = g.backup()
                        g.data[i][j]=cand
                        
                        while tryThis(g):
                            pass
                        if g.numOfZeros==0:
                            return False
                        else:
                            g.data = backupData

    for j in range(0,9):
        if g.zeros[9+j]==least0s:
            for i in range(0,9):
                if g.data[i][j]==0 and len(g.candidates[i][j])==leastCandids:
                    for cand in g.candidates[i][j]:
                        backupData = g.backup()
                        g.data[i][j]=cand
                        
                        while tryThis(g):
                            pass
                        if g.numOfZeros==0:
                            return False
                        else:
                            g.data = backupData
    for a in range(0,9):
        if g.zeros[18+a]==least0s:
            for i in range(3*(a//3),3*(a//3)+3):
                for j in range(3*(a%3),3*(a%3)+3):
                    if g.data[i][j]==0 and len(g.candidates[i][j])==leastCandids:
                        for cand in g.candidates[i][j]:
                            backupData = g.backup()
                            g.data[i][j]=cand
                            
                            while tryThis(g):
                                pass
                            if g.numOfZeros==0:
                                return False
                            else:
                                g.data = backupData
    '''
    '''
    for i in range(0,9):
        for j in range(0,9):
            if g.data[i][j]==0 and len(g.candidates[i][j])>0 and len(g.candidates[i][j])<leastCandids:
                leastCandids = len(g.candidates[i][j])
    '''
    '''
    for i in range(0,9):
        for j in range(0,9):
            if g.data[i][j]==0 and len(g.candidates[i][j]) == leastCandids:
                for cand in g.candidates[i][j]:
                    backupData = g.backup()
                    g.data[i][j]=cand
                    
                    while tryThis(g):
                        pass
                    if g.numOfZeros==0:
                        return False
                    else:
                        g.data = backupData
                        '''
    for i in range(0,9):
        for j in range(0,9):
            if g.data[i][j]==0:
                g.updateCandidate(i,j)
                for cand in g.candidates[i][j]:
                    g.data[i][j] = cand
                    if tryThis(g):
                        return True
                g.data[i][j]=0
                    
                    
    
    return False
                    
def asdf(g):
 

    (i,j)=g.missingLocation2()
    if (i,j)==(9,9):
        print("success")
        return True

    for cand in g.candidates[i][j]:
        g.data[i][j] = cand
        if asdf(g):
            return True
        g.data[i][j]=0
    return False


def asdf2(g):
    '''
    g.updateZeros()
    if g.numOfZeros==0:
        print("success")
        return True'''
    (i,j)=g.missingLocation()
    if (i,j)==(9,9):
        print("success")
        return True
    g.updateCandidate(i,j)
    for cand in g.candidates[i][j]:
        g.data[i][j]=cand
        if asdf2(g):
            return True
    g.data[i][j]=0
    return False

def solve(g):
    
    g.updateZeros()
    while tryThis(g):
        pass
    if g.numOfZeros==0:
        print("success")
    else:
        print("fail")
    print(g.data)

                
f = open("p096_sudoku.txt",'r')
data=f.read().split("Grid ")
for i in range(1,len(data)):
    rows=data[i].split('\n')
    g = grid(rows)
    grids.append(g)

    
f.close()
'''
t=time.time()
for i in range(0,9):
        for j in range(0,9):
            if grids[0].data[i][j]==0:
                grids[0].updateCandidate(i,j)
print(time.time()-t)

'''
t=time.time()
for g in grids:
    for i in range(0,9):
        for j in range(0,9):
            if g.data[i][j]==0:
                g.updateCandidate2(i,j)
    asdf(g)
print(time.time()-t)


total=0
for g in grids:
    s=''
    for i in range(0,3):
        s = s + str(g.data[0][i])
    total+=int(s)
print(total)
