#code

def isRotated(str1, str2):
    if len(str1) != len(str2):
        return False
    anticlockwise = ""
    clockwise = ""
    length = len(str2)
    anticlockwise = anticlockwise + str2[length-2:] + str2[:-2]
    clockwise = clockwise + str2[2:] + str2[:2]
    if (anticlockwise == str1) or (clockwise == str1):
        return True
    return False
        
N = int(input())
for i in range(N):
    str1 = input().strip()
    str2 = input().strip()
    res = isRotated(str1, str2)
    print(1) if res else print(0)