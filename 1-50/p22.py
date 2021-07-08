poof = open("p22_names.txt")
sum = 0
ln = poof.readline()
x = ln.split(',')

for i, j in enumerate(x):
    x[i] = x[i][1:len(j)-1]
#print(len(x))
x.sort()

for i, name in enumerate(x):
    score = 0
    for char in name:
        score += int(ord(char))-64
    score *= (i+1)
    sum += score

print(sum)