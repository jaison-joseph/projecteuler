s = 3
x = []

x[0][0] = 0

for i in range(1,s):
    x[0][i] = 1
    x[i][0] = 1

for i in range(1,s):
    for j in range(1,s):
        paths = 0
        paths += x[i-1][j]
        paths += x[i][j-1]

print(x)