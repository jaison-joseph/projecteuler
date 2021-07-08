from sys import exit
from itertools import permutations

primes = [2,3,5,7]
solution = 0
bad_boys = [2,3,4,6,8,9]

ideal = set()
ideal_list = []
for i in range(1,10):
    ideal.add(str(i))
    ideal_list.append(str(10-i))

def check_prime(num):
    sqrt = int(num ** 0.5)+1
    modlambda = (lambda x: num % x)
    loc = 0
    for n in primes:
        if n > sqrt:
            break
        if num % n == 0:
            return
    primes.append(num)

def check_pan(num):
    global misses
    global zerohero
    global ideal
    sqrt = int(num ** 0.5)+1

    loc = 0
    for n in primes:
        if n > sqrt:
            break
        if num % n == 0:
            return
    print("\n\n --------------- \n\n")
    print("solution is", num)
    exit()

lower = 123456789//6-1
upper = 987654321//6+1

prime_upper = int(1.5*(10**9)**0.5)//6 + 1
# prime_upper = 10**9//6+1


for i in range(2,prime_upper):
    check_prime(6*i-1)
    check_prime(6*i+1)

print("\n\n--------- \n\n")
print(primes[-1])
print(len(primes))

#last digit nonos: 2 4 6 8 3 9
# possible_solutions = [int(''.join(x)) for x in permutations(ideal_list) if int(''.join(x))%10 not in bad_boys]
start_index = 0
while True:
    possible_solutions = [int(''.join(x)) for x in permutations(ideal_list[start_index:])]
    print("numerb of opssibel solutions:", len(possible_solutions))
    for n in possible_solutions:
        check_pan(n)
    start_index += 1
# for i in range(upper, lower, -1):
#     check_pan(6*i+1)
#     check_pan(6*i-1)

print("you should not be reading this")
