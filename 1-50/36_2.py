solutions = []

for i in range(1,10**6):

    x = str(i)
    if x != x[::-1]:
        continue

    y = bin(i)[2:]
    if y != y[::-1]:
        continue

    solutions.append(i)

print(solutions)
print(len(solutions))
print(sum(solutions))
