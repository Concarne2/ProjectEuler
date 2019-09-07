mincoord=0
maxcoord=50
count=maxcoord**2
for x1 in range(mincoord,maxcoord+1):
    for y1 in range(mincoord,maxcoord+1):
       for x2 in range(mincoord,maxcoord+1):
           for y2 in range(mincoord,maxcoord+1):
               if (x1,y1)==(0,0) or (x2,y2)==(0,0) or (x1,y1)==(x2,y2):
                   pass
                
               elif y1 == 0:
                   if x2 == x1:
                       count+=1
               elif x2-x1!=0 and x1/y1 == -(y2-y1)/(x2-x1):
                   count+=1
                
print(count)
