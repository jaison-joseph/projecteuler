f = open("p042_words.txt",'r')
# print(f)

tris = []
for i in range(1,31):
    tris.append((i*(i+1))//2)

print(tris)

aa = ord('A')
def pos(x):
    return ord(x) - aa + 1
def n1(x):
    sum = 0
    for y in x:
        sum += pos(y)
    return sum

data = f.read().split(',')
data = [d[1:-1] for d in data]
sums = list(map(n1, data))
final = [d for d in sums if d in tris]
print(len(data))
print(len(sums))
print(len(final))
for i in range(10):
    print(data[i], "::", sums[i])
