from decimal import *

getcontext().prec = 200 #setting decimal length

def pat_len(x, debug = 0):
    length = 0
    dec_str = str(Decimal(1)/Decimal(x))
    dec_str = dec_str[dec_str.find('.')+1:]
    if debug is 1: print(dec_str)
    for i in range(1,len(dec_str)//2):
        if debug is 1: print(dec_str[:i], " :: ", dec_str[i:2*i])
        if dec_str[:i] == dec_str[i:2*i]:
            length = i
            break
    if debug is 1: print("1 / ", str(x), ": ", length) 
    return length       


#print(Decimal(1)/Decimal(7))
longest = 0
longest_num = 0
for i in range (1,1000):
    l = pat_len(i)
    if (l>longest):
        longest = l
        longest_num = i

print("Longest num: ", longest_num, " :: length: ", longest)
pat_len(longest_num,1)