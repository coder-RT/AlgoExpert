#code

def sqrDist(p, q):
    return ((p[0] - q[0]) * (p[0] - q[0])) + ((p[1] - q[1]) * (p[1] - q[1]))

    
def checkSquare(p1, p2, p3, p4):
    d2 = sqrDist(p1, p2)
    d3 = sqrDist(p1, p3)
    d4 = sqrDist(p1, p4)
    if d2 == 0 or d3 == 0 or d4 == 0:
        print("No")

    if (d2 == d4) and (d2*2 == d3) and d2*2 == sqrDist(p2,p4):
        d = sqrDist(p2,p3)
        print("Yes") if ((d == sqrDist(p3, p4)) and (d == d2)) else print("No")

    if (d2 == d3) and (d2*2 == d4) and (d2*2 == sqrDist(p2, p3)) :
        d = sqrDist(p2, p4)
        print("Yes") if ((d==d2) and d== sqrDist(p3, p4)) else print("No")

    if (d3 == d4) and (d3*2 == d2) and (d3*2 == sqrDist(p3, p4)):
        d = sqrDist(p2, p3)
        print("Yes") if ((d == d3) and (d == sqrDist(p2, p4))) else print("No")

N = int(input())

for i in range(N):
    ipStr = [int(elem) for elem in input().strip().split(' ')]
    p1 = [ipStr[0], ipStr[1]]
    p2 = [ipStr[2], ipStr[3]]
    p3 = [ipStr[4], ipStr[5]]
    p4 = [ipStr[6], ipStr[7]]
    checkSquare(p1, p2, p3, p4)