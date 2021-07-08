
sizes = [[9,1]] #each entry is of the format: [<number of entries> <length of each entry>]
count = 9
pow = 1
while count <= 10**6:
    number_of_digits = 10**(pow+1) - 10**(pow)
    length = len(str(10**pow))
    sizes.append([number_of_digits, length])
    count += number_of_digits*length
    pow += 1

print(sizes)
print(count)

def digit_at_position(position):
    global sizes
    count = 0
    index = 0
    offset = 0
    set_info = []
    for index, info in enumerate(sizes):
        count += info[0]*info[1]
        if count > position:
            offset = position - (count - info[0]*info[1])
            set_info = info
            break
    second_offset = offset // set_info[1]
    num = 10**(set_info[1]-1) + second_offset - 1
    print("to find the digit at::",position)
    print("set_info::",set_info)
    print("offset::", offset)
    print("second_offset::", second_offset)
    print("num::", num)
    print("offset % set_info[1]::", offset % set_info[1])
    if offset % set_info[1] != 0:
        num += 1
        return str(num)[offset % set_info[1] - 1]
    else:
        return str(num)[-1]

prod = 1
for i in range(7):
    prod *= int(digit_at_position(10**i))

print("answer: ", prod)
