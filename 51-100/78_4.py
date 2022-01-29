lengths = [0,1,2]

current = 3
dupli = 0
half = 0
while current != 6:
    ct = 0
    dupli = current
    half = current // 2
    if current % 2 == 0:
        half += 1
    ct += half
    print(current,"::",half, "::", lengths[:half])
    ct += sum(lengths[:half])
    lengths.append(ct)
    current += 1

print(lengths)

'''

'''
