from itertools import permutations

# 1,4,4
# [1*1001=1001]
# [2*4999=9998]
# [1-9]*[1001-4999]
# 9 * 3999 = 35991
#
# 2,3,4
# [10*100=1000]
# [10*990=9990]
# [10-99]*[100-999]
# 90 * 900 = 81000

count = 0

answers = []

nums = ['1','2','3','4','5','6','7','8','9']

def fill_permutations(x):
    global count
    if x == 1:      #the 1,4,4 case
        obj = permutations(nums)
        f = ''
        for combo in obj:
            f = ''.join(combo)
            if int(f[0]) * int(f[1:5]) == int(f[5:]):
                answers.append((int(f[0]), int(f[1:5]), int(f[5:])))
                count = count + 1

    else:      #the 2,3,4 case
        obj = permutations(nums)
        f = ''
        for combo in obj:
            f = ''.join(combo)
            if int(f[:2]) * int(f[2:5]) == int(f[5:]):
                answers.append((int(f[:2]), int(f[2:5]), int(f[5:])))
                count = count + 1

fill_permutations(1)
fill_permutations(2)
sum = 0
for i in answers:
    sum += i[2]
print(answers)
print(sum)
