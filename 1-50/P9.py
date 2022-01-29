# to find pythagorean triplet 
count = 0
a = 1
keepgoing = True
while keepgoing:
    b = 1
    secondkeepgoing = True
    while secondkeepgoing:
        c = float((a**2 + b**2)**0.5)
        count += 1
        if a + b == c and a + b + int(c) == 1000:
            print("gotcha")
            # print("{} : {} : {}".format(a, b, c))
            keepgoing = False
            secondkeepgoing = False
        b += 1
        if a + b > 1000:
            secondkeepgoing = False
    if a > 1000:
        keepgoing = False
    a += 1

print(count)  