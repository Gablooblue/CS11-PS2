def findQuadrant(x,y):
    if x > 0 and y > 0:
        return "I"
    elif x >0 and y < 0:
        return "IV"
    elif x < 0 and y > 0:
        return "II"
    else:
        return "III"
    
def getNumber(s):
    num = ""
    for c in s: #for characters in string s
        if(c != '[' and c != ']'):
            num += c
    return int(num)

def calc(a):
    b = []
    for i in a:
        for j in i:
            b.append(j.split(","))
    
    x = getNumber(b[0][0]) + getNumber(b[1][0]) # x1 + x2
    y = getNumber(b[0][1]) + getNumber(b[1][1]) # y1 + y2
    output = "[" + str(x) + "," + str(y) + "]"
    print(output, end = " ")
    print(findQuadrant(x,y))
    
n = int(input())
a = []
for i in range(n):
    line = input()        
    a.append(line.split())
    calc(a)
    a = []
