def make_pentagonal(x):
    return int(x * (3*x-1) / 2)

numbers = []

for i in range(1,10000):
    numbers.append(make_pentagonal(i))

# print(numbers)

upper = len(numbers)//3 - 1

possible_solutions = []

for i in range(upper):
    current = numbers[i]
    x = [[abs(y - current), y + current, current, y]\
        for ind, y in enumerate(numbers[i+1:])\
        if abs(y - current) in numbers and y + current in numbers]
    if len(x) == 0:
        continue
    possible_solutions = x
    break


print(possible_solutions)

'''
  (x * (3*x-1) / 2) + (y * (3*y-1) / 2) = (z * (3*z-1) / 2)
  3x**2+3y**2
'''
