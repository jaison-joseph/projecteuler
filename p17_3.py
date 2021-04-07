one10 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
eleven19 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ten100 = ["ten", "twenty","thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]

nos = []
length = 0

for i in range(100):
    nos.append("")

for i, j in enumerate(one10): #1 to 9
    nos[i] = j

for i, j in enumerate(eleven19): #11 to 19
    nos[i+10] = j

for i, j in enumerate(ten100): # 10 20 ... 100
    nos[10*i + 9] = j
    if (i>0 and i<9):
        for k in range(9):
            nos[10*(i+1) + k] = (j+one10[k])

for i, j in enumerate(nos):
    length += len(j)
    if (i%10) == 0: print('\n')
    print(j)

length += 9*length #the rest of the nums
for i, j in enumerate(one10):
    length += 99*(len(j)+10)

for i in one10: #for the 1st word in 100's
    length += len(i)

length += 11 #for the onethousand
length -= 7 #for the 10th hundred 

print('\n', length)