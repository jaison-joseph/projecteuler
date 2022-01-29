'''
number = 1
factors = []
for i in range (10, 1, -1):
    flag = 1
    for j in factors:
        if j%i == 0:
            flag = 0
    if flag == 1:
        factors.append(i)
        number *= i

print(number)
print(factors)


number = 1
factors = []  
for i in range(1, 11):
    flag = 1
    for j in factors:
        if flag == 1:
            for k in factors:
                if j*k == i:
                    if j == k:
                        factors.remove(j)
                    else:
                        flag = 0
                        break
        else:
            break
    
    if flag == 1:
        factors.append(i)
        number *= i

print(number)
print(factors)
'''
'''
factors = [2,3,4,5,6,7,8,9,10]
blacklist =[]
for i in factors:
    for j in factors:
        if i*j in factors:
            blacklist.append(j)
            if i!=j:
                blacklist.append(i)         
            break     

print(blacklist)
'''

def gcd(x, y):
    i = 1
    the = 1
    while i<=x and i<=y:
        i += 1
        if x%i == 0 and y%i == 0:
            the = i
    
    return the

#print(gcd(20,10))


product = 1
to_multiply = [2,3,4,5,6,7,8,9,10]
for i in range(1,21):
    to_divide = gcd(i,product)
    product = product * i / to_divide

print(product)