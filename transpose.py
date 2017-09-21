a = input()
a = a.split()
rows = int(a[0])
cols = int(a[1])

#Creating a 2d matrix
Matrix = [[0 for x in range(rows)] for y in range(cols)]

#Getting input
for j in range(rows):
    curr = input()
    curr = curr.split()
    for i in range(cols):
        Matrix[i][j] = curr[i]

#Flipping cols and rows
for i in range(cols):
    for j in range(rows):
        print(Matrix[i][j], end = " ")
    print()
