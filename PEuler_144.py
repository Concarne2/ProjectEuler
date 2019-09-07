#slope of the incident ray
m = 0

#slope of the tangent
t = 0

#slope of the 법선
n = 0

#slope of the reflecting ray
s = 0

def TangentFromPoint(p):
    tangent = -4*p[0]/p[1]
    return tangent

point1 = (0,10.1)
point2 = (1.4,-9.6)

def GetNextPoint(point1, point2):

    m = (point1[1] - point2[1]) / (point1[0] - point2[0])

    t = TangentFromPoint(point2)

    n = -1/t

    s = (-m*n*n + m -2*n)/(n*n - 2*m*n-1)

    point1 = point2

    a = 4+s*s
    b = 2 * s * (point1[1] - s*point1[0])

    newX = -b/a - point1[0]
    newY = s*(newX - point1[0]) + point1[1]

    point2 = (newX,newY)

    return point2
count = 0
while True:
    newPoint = GetNextPoint(point1, point2)
    count+=1
    if newPoint[0] >= -0.01 and newPoint[0] <= 0.01 and newPoint[1]>0:
        print(count)
        break
    point1 = point2
    point2 = newPoint

