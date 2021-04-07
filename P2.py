sum = 0
num1 = 1
num2 = 2
while num1 < 4000000:
    if num1%2 == 0:
        sum += num1
    num3 = num2
    num2 = num1 + num2
    num1 = num3

print(sum)
    