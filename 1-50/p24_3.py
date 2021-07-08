import math
use = []
nums = []
for i in range (10): nums.append(0)


def possible():
    count = []
    for i in range (10):
        if use[i] == 0: count.append(i)
    return count


id = 1000000
danum = ''
sum = 0
for i in range (9,0,-1):
    div = id // math.factorial(i)
    print(div *math.factorial(i) )
    sum += div * math.factorial(i)
    if (div%math.factorial(i)==0): use.append(0)
    else: use.append(div+1)
    id -= div * math.factorial(i)

print(use)
print(sum)
'''
for i in range(10):
    inc = 0
    for j in range (10):
        if (inc == use[i]): break
        if (nums[j]==0): inc += 1
    
    print(j)


print(use)
'''