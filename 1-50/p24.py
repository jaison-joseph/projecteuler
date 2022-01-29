import math

nos = []
for i in range (10): nos.append(0)

id = 0
danum = ''
for i in range(10): #just for the 10 digits, also used for factorial
    j = 0
    count = 0
    while id < 1000000 and count < 10:
        id += math.factorial(9-i)
        count += 1

    idb4 = id
    #print(count)

    if (count == 10):
        count -= 1
        id -= math.factorial(9-i)
        
    while (id > 1000000 or nos[count]==1):
        id -= math.factorial(9-i)
        count -=1 

    danum += str(count)
    nos[count] = 1

    print(idb4, ": ", id, ": ", danum)

    if (id == 1000000):
        break

print(danum)



