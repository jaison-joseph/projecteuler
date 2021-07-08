solutions = []

start_and_end = []

#filling up start_and_end with 1 to 9
for i in range(1,10):
    start_and_end.append(i)

for num in range(1,10):
    bin_str = bin(num)[2:]
    if bin_str == bin_str[::-1]:
        solutions.append(num)

for i in range(0,10**4):
    x = str(i)
    if x != x[::-1]:
        continue
    for j in start_and_end:
        num = j*10**(len(x)+1) + i*10 + j
        bin_str = bin(num)[2:]
        if bin_str == bin_str[::-1]:
            solutions.append(num)

print(solutions)
print(len(solutions))
print(sum(solutions))

# for num in solutions:
#     bin_str = bin(num)[2:]
#     print("bin: ", bin_str)
#     print(bin_str == bin_str[::-1])
