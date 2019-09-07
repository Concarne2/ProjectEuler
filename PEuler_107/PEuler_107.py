DIM = 40

mat = []

f = open("p107_network.txt","r")

for i in range(0,DIM):
    line = f.readline().strip().split(",")
    numline=[]
    for c in line:
        if c == '-':
            numline.append(0)
        else:
            numline.append(int(c))
    mat.append(numline)

f.close()

def FindMin():
    minv = 10000
    pair=(DIM,DIM)
    for r in range(0,DIM):
        for c in range(0,DIM):
            if mat[r][c]!=0 and ((mat[r][c]) < minv):
                minv = mat[r][c]
                pair=(r,c)
    return pair

def FindNextConnection():
    minv = 10000
    pair=(DIM,DIM)
    for r in range(0,DIM):
        if connected[r]:
            for c in range(0,DIM):
                if mat[r][c]!=0 and ((mat[r][c]) < minv) and not connected[c] :
                    minv = mat[r][c]
                    pair=(r,c)
    return pair

def FullyConnected():
    return not (False in connected.values())
    

connections=[]
connected={}
for i in range(0,DIM):
    connected[i] = False

connections.append(FindMin())

connected[connections[0][0]] = True
connected[connections[0][1]] = True

while not FullyConnected():
    connections.append(FindNextConnection())
    connected[connections[-1][0]] = True
    connected[connections[-1][1]] = True

totalLen=0
for con in connections:
    totalLen+=mat[con[0]][con[1]]

totaltotal=0
for row in mat:
    totaltotal+=sum(row)
totaltotal /=2
'''
def Next():
    connections.append(FindNextConnection())
    print(connections[-1])
    connected[connections[-1][0]] = True
    connected[connections[-1][1]] = True'''
