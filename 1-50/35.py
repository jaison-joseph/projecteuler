primes = [2,3]

solutions = []

def check_prime(num):
    sqrt = int(num ** 0.5)+1
    for i in primes:
        if num % i == 0:
            return
        if i > sqrt:
            break
    primes.append(num)

# def check_rotations(num):
#     foo = str(num)
#     locations = [primes.index(num)]
#     for i in range(1,len(foo)):
#         naya = int(foo[i:] + foo[:i])
#         # print("naya: ",naya)
#         try:
#             locations.append(primes.index(naya))
#         except ValueError:
#             return
#     for loc in locations:
#         del primes[loc]
#     solutions.append(num)

def check_rotations(num):
    foo = str(num)
    for i in range(1,len(foo)):
        naya = int(foo[i:] + foo[:i])
        if naya not in primes:
            return
    solutions.append(num)


upper = 10**6//6+1

for i in range(1,upper):
    check_prime(6*i-1)
    check_prime(6*i+1)

print("done generating primes")

for i in primes:
    check_rotations(i)


print(primes[:50])
# print(solutions)
print(len(solutions))
print(971 in primes)
