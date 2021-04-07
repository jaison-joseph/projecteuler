x = pow(2,1000)
print(x)
sum = 0
while (x>0):
    sum += x%10
    x = x//10
print(sum)