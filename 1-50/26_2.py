import math

def decimal(divisor, length):
    
    dividend = 1
    dec = [] #array consisting of length entries of the decimal places
    
    for i in range (length+1):
        q = dividend // divisor   
        dividend = dividend - q * divisor
        dividend = dividend * 10
        dec.append(q)
    
    ret_string = ''
    for i in dec[1:]:
        ret_string = ret_string + str(i)
    
    if divisor < 10:
        return ret_string[1:]
    elif divisor < 100:
        return ret_string[2:]
    else:
        return ret_string[3:]

def occurence(foo):
    dec_length = 4000
    dec = decimal(foo,dec_length)
    #print(dec[:100])
    for i in range(1,dec_length//2+1):
        if dec[:i] == dec[i:2*i]:
            return dec[:i]
    return dec[:100]

pows_of_two = []
for i in range(1,math.floor(math.log(1000,2))):
    pows_of_two.append(2**i)


pows_of_five = []
for i in range(1,math.floor(math.log(1000,5))):
    pows_of_five.append(5**i)

max_len = -1
max_div = -1

for i in range (2,1001):
    if i in pows_of_two:
        continue
    if i in pows_of_five:
        continue
    f = occurence(i)
    if len(f) > max_len:
        max_len = len(f)
        max_div = i

print("asdf: ", max_len)
print("asdf: ", max_div)

print(occurence(max_div))




