t = [1,2,3,4,5,7,8]
sums = [0]
for i in range(len(t)):
    for j in range(i, len(t)):
        temp = t[i] + t[j]
        if (temp < 28123):
            canWrite= 1
            for k in range(len(sums)):
                if (sums[k] > temp): break
                if (sums[k]==temp):
                    canWrite = 0 
                    break
            #if (k == len(sums)-1 and canWrite == 1): sums.append(temp)
            if canWrite == 1: sums.insert(k,temp)
        else: break

print("Sums len: ", len(sums))
print(sums)

t.insert(5,222)
print(t)