
sq_sum = 0
sumto_sq = 0
for i in range (1,101):
    sq_sum += (i*i)
    sumto_sq += i

final = (sumto_sq * sumto_sq) - sq_sum
print(final)