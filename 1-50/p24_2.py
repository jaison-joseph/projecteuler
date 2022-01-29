import math


id = 0
used = ''
danum = ''
for i in range(10): #just for the 10 digits, also used for factorial
    j = 0
    count = 0
    while id < 1000000 and count < 10:
        id += math.factorial(9-i)
        count += 1

    while str(count) in danum or id > 1000000:
        id -= math.factorial(9-i)
        count -= 1
        if count == 0: break
    
    #if count == 0: danum += '0' 
    danum += str(count)

print(danum)