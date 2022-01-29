len = 0
starter_1 = [3,3,5,4,4,3,5,5,4]
starter_2 = [6,6,8,8,7,7,9,8,8]
teners = [3,6,6,5,5,5,6,6,6,7]

#until 9
for num in starter_1:
    len += num

#10
len += teners[0]

#11 - 19
for num in starter_2:
    len += num

#20
len += teners[1]

#until 100
for x in range(21,101):
    if (x%10 == 0):
        len += teners[x//10-1]
    else:
        len += starter_1[(x%10)-1]
        len += starter_1[(x//10)-1]

#until 99, exclusing the multiples of 100
for x in starter_1:
    len += ( 100*x + 10 ) 

#multiples of 100, excluding 1000
for x in starter_1:
    len += (x + 7)

#1000
len += 11

print(len)