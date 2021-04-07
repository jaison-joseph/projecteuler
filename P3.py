def isprime(num):
    flag = 0
    for i in range (2, int((num/2)+1)):
        if num % i == 0:
            #print(i)
            flag = 1
            break
    return flag

def largestpf(num):
    val = 2
    for i in range (2, int((num/2)+1)):
        #print(i)
        if num % i == 0 and isprime(i) == 0:
            val = i
            
    print(val)

#largestpf(60085429)

def improvedpf(num):
    val = 2
    for i in range (2, int((num/2)+1)):
        if num % i == 0 and isprime(i) == 0:
            val = i
            num = num / i
            
    print(val)

#improvedpf(60085429)

def improvedpf2(num):
    alsonum = num
    val = 2
    prod = 1
    for i in range (2, int((num/2)+1)):
        if num % i == 0 and isprime(i) == 0 and prod != alsonum:
            val = i
            prod *= i
            num /= i
    print(prod)
    print(val)

#improvedpf2(600851475143)

def firsthundred():
    prod = 1
    primearray = []
    for i in range (2, 20000):
        if isprime(i) == 0:
            #print(i)
            prod *= i
            primearray.append(i)
    return prod, primearray

a, b = firsthundred()
print(b)

num = 600851475143
for i in b:
    if num % i == 0:
        print('Divisible by :{}'.format(i))
        num /= i
        print('Number is now: {} \n'.format(num))
    
    #else:
        #print('no \n')
        


