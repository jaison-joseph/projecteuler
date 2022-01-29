lengths = []
greatest = 0
big_num = 0
for i in range (1,1000001):
    length = 0
    j = i
    while (j!=1):
        if j%2==0:
            j /= 2
        else:
            j = (3*j + 1)
        length += 1
        if (j<i):
            length += lengths[int(j-1)]
            break
    lengths.append(length)
    if length > greatest: 
        greatest = length
        big_num = i
        print(i, ": ", length)