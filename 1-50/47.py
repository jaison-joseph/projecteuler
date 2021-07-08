from math import sqrt, floor, ceil

solutions = [[0],[1],[2],[3],[2,2]]
solutions = [set(x) for x in solutions]

primes = [2,3]

streak = 0

def checkPrime(num):
    global streak
    upper = ceil(sqrt(num))+1
    for x in primes:
        if x > upper:
            break
        if num % x == 0:
            solutions.append(set([x]+list(solutions[num//x])))
            if len(solutions[-1]) == 4:
                streak += 1
                if streak == 4:
                    print("solution is: ", num)
                    exit(0)
            else:
                streak = 0
            return
    primes.append(num)
    streak = 0
    solutions.append({num})

i = 5
while True:
    checkPrime(i)
    i += 1

# print(primes)
# for index, x in enumerate(solutions):
#     print(index, "::", x, "::")
