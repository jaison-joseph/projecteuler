nos = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

count = 0
a = []
b = []
row = 0
for i, j in enumerate(nos):
    if j == ' ':
        a.append(int(nos[i-2:i]))
    if j== '\n':
        a.append(int(nos[i-2:i]))
        b.append(a)
        a  = []

print(b)
current_indice = 0
sum = 0

b_2 = b[::-1]
print(b_2)

for k in range(len(b_2)-1):
    i = b_2[k]
    for j in range(len(i)-1):
        b_2[k+1][j] += i[j] if (i[j] > i[j+1]) else i[j+1]
        #b_2[k][j] = 0

print(b_2)
    
    
