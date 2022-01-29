import math

triplets = []

sum = 0
count = 0
hypotenuse = 5
while sum < 1000:
    lower = int(hypotenuse**0.5)-1
    for s1 in range(hypotenuse-1,lower,-1):
        s2 = hypotenuse**2 - s1**2
        sqrt_s2 = math.isqrt(s2)
        if s2 == sqrt_s2**2:
            triplets.append([hypotenuse, s1, sqrt_s2])
            sum = hypotenuse + s1 + sqrt_s2
            count += 1
            break
    hypotenuse += 1

# print(triplets)
print(len(triplets))

sums = []

for trio in triplets:
    sum = 0
    for num in trio:
        sum += num
    sums.append(sum)

unique_sums = set(sums)

unique_sum_count = []

largest = -1
frequency = -1

for uni_sum in unique_sums:
    ct = sums.count(uni_sum)
    unique_sum_count.append(ct)
    if ct > frequency:
        largest = uni_sum
        frequency = ct

print(largest)
print(frequency)
