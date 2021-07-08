from itertools import combinations

# replacements = [list(combinations([1,2,3,4], i)) for i in range(1,5)]
# replacements = [list(combinations([1], i)) for i in range(1,5)]

'''
primes_2 contains the primes with 6 digits

so, for a potential solution candidate,
the number being repalced must be with a higher digit.
if lower, it would have been encountered previously in the list of primes
hence, for upto 8 replacements, the same digit being replaced must be in [0.1.2]
'''

primes_1 = [2,3,5,7]
primes_2 = []

# the index is the digit and the value
# at the index is the number of occurences of that digit
def counter(num):
    counts = [0,0,0]
    num = num // 10
    dig = 0
    for i in range(4):
        dig = num % 10
        if dig == 0:
            counts[0] += 1
        elif dig == 1:
            counts[1] += 1
        elif dig == 2:
            counts[2] += 1
        num = num // 10
    return counts

def checkPrimes_1(i):
    n = 6 * i - 1
    upper = int(n**0.5)
    for p in primes_1:
        if n % p == 0:
            break
        if p > upper:
            primes_1.append(n)
            break

    n += 2
    for p in primes_1:
        if n % p == 0:
            return
        if p > upper:
            primes_1.append(n)
            return

def checkPrimes_2(i):
    n = 6 * i - 1
    upper = int(n**0.5)+2
    for p in primes_1:
        if n % p == 0:
            break
        if p > upper:
            primes_2.append(n)
            break

    n += 2
    for p in primes_1:
        if n % p == 0:
            return
        if p > upper:
            primes_2.append(n)
            return

#generating primes
# for i in range(1, 20):
for i in range(2, 10**5//6+1):
    checkPrimes_1(i)

for i in range(10**5//6+1, 10**6//6+1):
    checkPrimes_2(i)

print("primes_1")
print(primes_1[-10:])
print(primes_1[:10])
print(len(primes_1))

print("primes_2")
print(primes_2[-10:])
print(primes_2[:10])
print(len(primes_2))


foo = []
matches = 0
index = 0
replaced = 0

for number in primes_2:
    counts = counter(number)
    if max(counts) < 2:
        continue
    index = counts.index(max(counts))
    matches = 0
    for newDig in range(index, 10):
        replaced = int(str(number).replace(str(index), str(newDig)))
        if replaced in primes_2:
            matches += 1
    if matches > 7:
        print(number)
        break

print("end of program")
