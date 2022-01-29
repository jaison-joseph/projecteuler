nums = []
for i in range(10,100):
    nums.append(i)

solutions = []

#num and den are 2 digit numbers
for num in nums:
    for den in nums:
        if num == den:
            continue
        if str(num)[::-1] == str(den):
            continue
        if num % 11 == 0 or den % 11 == 0:
            continue
        s1 = {str(num)[0], str(num)[1]}
        s2 = {str(den)[0], str(den)[1]}
        common = s1.intersection(s2)
        if len(common) == 0:
            continue
        s1 = s1 - common
        s2 = s2 - common
        #now s1 and s2 have 1 element
        try:
            if int(s1.pop()) / int(s2.pop()) == num / den and num < den and num % 10 != 0 and den % 10 != 0:
                solutions.append([num,den])
        except ZeroDivisionError:
            print(num, "::", den)
            continue
print(solutions)
print(len(solutions))
