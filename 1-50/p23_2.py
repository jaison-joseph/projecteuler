nos = [] #the abundant nos
nonos = []
sum = 0
count = 0
f1 = 0
f2 = 0

def sum_d(x):
    sum = 0
    for i in range(1,x//2+1):
        if (x%i==0):
            sum += i
    return sum

for i in range(12,28123):
    if (sum_d(i)>i): nos.append(i)

for i in range (len(nos)):
    j=i
    while j<len(nos):
        t = nos[i]+nos[j]
        if t <= 28123:
            count += 1
            nonos.append(t)  
        else:
            break
        j+=1

temp = list(set(nonos))

for i in temp:
    f1 += i

for i in range (28124):
    f2 += i

print(len(nonos))
print(len(temp))
print(f2, ", ", f1)
