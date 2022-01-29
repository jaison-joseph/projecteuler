def sums(num):
    s = 1
    for i in range(2,num//2+1):
        if num%i==0: s += i

    return s

print(sums(220))
#

nos = []
for i in range(1,10001):
    nos.append(sums(i))
    print (nos[-1], end = "\n")
#
# #for i in range(20):
# #  print(i+1, ": ", nos[i])
#
# print("1000, ", nos[283])
#
# x=0
# for i, j in enumerate(nos):
#     num_1 = i+1
#     val_1 = j
#
#     num_2 = j
#     val_2 = 0
#     if (j<=10000 and val_1 != 0):
#         val_2 = nos[j-1]
#     if num_1 == val_2 and num_2 == val_1 and num_1 != num_2:
#         print(num_1, ", ",val_1, " :: ",num_2, ", ", val_2, ", ")
#         x += num_1
#         x += num_2
#         nos[j-1] = 0
#
# print(x)
