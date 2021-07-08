starters = []

bigboy = -1
answer = -1
'''
11
21
31
41
51
61
71
81
91  2
'''

for i in range(1,102):
    starters.append(i)

for num in starters:
    if num > 99:
        snaps = []
        multiplier = 2
        prod = num * multiplier
        while prod < 1000:
            snaps.append(prod)
            multiplier += 1
            prod = num * multiplier
        print(snaps)
        for i in range(0,len(snaps)-len(snaps)%2):
            print(snaps[])
    elif num > 9:
        start = 2   #the starting number in the sequence
        while True:
            x = ''
            for i in range(1,4):
                x = x + str((i+start)*num)
            if int(x) > bigboy:
                bigboy = int(x)
                answer = num
            break
            start = start + 1

#for the numbers

print("bigboy: ", bigboy)
print("answer: ", answer)
