primes = [2,3]

solutions = []

count = 0

def check_prime(num):
    sqrt = int(num ** 0.5)+1
    for i in primes:
        if num % i == 0:
            return
        if i > sqrt:
            break
    primes.append(num)
    check_slices(num)

def check_slices(num):
    global count
    x = str(num)
    for i in range(1,len(x)):
        if int(x[i:]) not in primes:
            return
        if int(x[:i]) not in primes:
            return
    solutions.append(num)
    count = count + 1

i = 1

while count < 13:
    check_prime(6*i-1)
    check_prime(6*i+1)
    i = i + 1

print(solutions)
print(len(solutions))
print(sum(solutions))
