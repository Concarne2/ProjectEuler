SIZE = 80

f = open("p083_matrix.txt","r")

rows = f.readlines()

mat=[]


for line in rows:
    mat.append(line.split(","))

for i in range(0,len(mat)):
    for j in range(0,len(mat[0])):
        mat[i][j]=int(mat[i][j].strip())

class PriorityQueue(object):
    
    def __init__(self): 
        self.queue = []
        self.isHere=[]
        for i in range(0,SIZE):
            here=[]
            for j in range(0,SIZE):
                here.append(False)
            self.isHere.append(here)
        
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data):
        if self.isHere[data[1]][data[2]]:
            self.rid(data[1],data[2])
        else:
            self.isHere[data[1]][data[2]]=True
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def pop(self): 
        try: 
            minimum = 0
            for i in range(len(self.queue)): 
                if self.queue[i][0] < self.queue[minimum][0]: 
                     minimum = i 
            item = self.queue[minimum] 
            del self.queue[minimum] 
            return item 
        except IndexError: 
            print() 
            exit()
    def rid(self,i,j):
        for ind in range(len(self.queue)):
            if self.queue[ind][1]==i and self.queue[ind][2]==j:
                del self.queue[ind]
  

curr=0,0

distances=[]
visited=[]

for i in range(0,SIZE):
    distance=[]
    visit=[]
    for j in range(0,SIZE):
        distance.append(-1)
        visit.append(False)
    distances.append(distance)
    visited.append(visit)

distances[0][0]=mat[0][0]

PQ = PriorityQueue()

def dijkstra(i,j,size):
    i=curr[0]
    j=curr[1]

    if i != size-1:
        if not visited[i+1][j]:
            if distances[i+1][j]==-1:
                distances[i+1][j]=distances[i][j]+mat[i+1][j]
                PQ.insert((distances[i+1][j],i+1,j))
            elif distances[i+1][j] > distances[i][j]+mat[i+1][j]:
                distances[i+1][j] = distances[i][j]+mat[i+1][j]
                PQ.insert((distances[i+1][j],i+1,j))
    if j != size-1:
        if not visited[i][j+1]:
            if distances[i][j+1]==-1:
                distances[i][j+1]=distances[i][j]+mat[i][j+1]
                PQ.insert((distances[i][j+1],i,j+1))
            elif distances[i][j+1] > distances[i][j]+mat[i][j+1]:
                distances[i][j+1] = distances[i][j]+mat[i][j+1]
                PQ.insert((distances[i][j+1],i,j+1))
    if i != 0:
        if not visited[i-1][j]:
            if distances[i-1][j]==-1:
                distances[i-1][j]=distances[i][j]+mat[i-1][j]
                PQ.insert((distances[i-1][j],i-1,j))
            elif distances[i-1][j] > distances[i][j]+mat[i-1][j]:
                distances[i-1][j] = distances[i][j]+mat[i-1][j]
                PQ.insert((distances[i-1][j],i-1,j))
    if j != 0:
        if not visited[i][j-1]:
            if distances[i][j-1]==-1:
                distances[i][j-1]=distances[i][j]+mat[i][j-1]
                PQ.insert((distances[i][j-1],i,j-1))
            elif distances[i][j-1] > distances[i][j]+mat[i][j-1]:
                distances[i][j-1] = distances[i][j]+mat[i][j-1]
                PQ.insert((distances[i][j-1],i,j-1))

    visited[i][j] = True
   # print(str(i)+", "+str(j))
    currnode = PQ.pop()
   # print(currnode)
    return currnode[1],currnode[2]

while curr!=(SIZE-1,SIZE-1):
    curr=dijkstra(curr[0],curr[1],SIZE)

print(distances[SIZE-1][SIZE-1])




