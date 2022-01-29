def isprime(num):
    flag = True
    for i in range (2, int((num/2)+1)):
        if num % i == 0:
            #print(i)
            flag = False
            break
    return flag

counter = 1
prime_check = 2
while counter <= 10001:
    if isprime(prime_check):
        counter += 1
    prime_check += 1

print(prime_check - 1)

