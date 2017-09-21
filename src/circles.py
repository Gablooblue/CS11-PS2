def getDistance(x1 ,y1, x2, y2):
    a = int(x2) - int(x1)
    b = int(y2) - int(y1)
    c= (a ** 2 + b ** 2)**(1/2.0)
    return c

x = []
for i in range(2):
    n = input()
    n = n.split()
    x.append(n)

#Yeah this part is really ugly
#Probably could've been done better but was rushing
x1 = x[0][0]
x2 = x[1][0]
y1 = x[0][1]
y2 = x[1][1]
r1 = x[0][2]
r2 = x[1][2]

#distance - radius
dist = getDistance(x1 ,y1, x2, y2) - (float(r1) + float(r2))
if dist == 0:
    print("Tangent")
elif dist < 0:
    print("Intersecting")
else:
    print("Neither")
