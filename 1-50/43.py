from itertools import permutations

ideal_list = [str(x) for x in range(10)]

limit = 10**9

dividers = [2,3,5,7,11,13,17]

sum = 0
solutions = []

def tester(x):
    global sum, solutions
    # print("x::",x)
    for i in range(1,8):
        # print(x[i:i+3])
        if int(x[i:i+3])%dividers[i-1] != 0:
            return
    sum += int(x)
    solutions.append(int(x))

possible_solutions = [''.join(x) for x in permutations(ideal_list) if int(''.join(x)) > limit]
print(len(possible_solutions))
for i in possible_solutions:
    tester(i)
print(sum)
print(solutions[:10])
