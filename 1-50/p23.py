def s(x):
    sum = 1
    for i in range(2,x//2+1):
        if x%i==0: sum += i
        if sum > x: break
    return sum

n = []
sums = [0]

#fill abds
for i in range(12,28123):
    if (s(i)>i): 
        n.append(i)
        
#fill sums    
for i in range(len(n)):
    for j in range(i, len(n)):
        temp = n[i] + n[j]
        if (temp < 28123):
            canWrite= 1
            for k in range(len(sums)):
                if (sums[k] > temp): break
                if (sums[k]==temp):
                    canWrite = 0 
                    break
            if (k == len(sums)-1 and canWrite == 1): sums.append(temp)
            elif canWrite == 1: sums.insert(k-1,temp)
        else: break

'''    
for i , no1 in enumerate(abds):
    for j in range (i,len(abds)):
        t = no1 + abds[j]
        if t <= 200:
            k=0
            while (k<len(sums) and t<sums[k]): k+=1
            if (sums[k] > t): sums.insert(k-1,t)
            if (k == len(sums) and t!=sums[k]): sums.insert(k-1,t)
            
        else: break
'''


print("abds len: ", len(n))
print("sums len: ", len(sums))

print(n[len(n)-1])
print(sums[len(sums)-1])

#print(sums)

count = 0
sum = 0
'''
sums.sort()
j = 0
for i in range(1,28124):
    if i<=sums[j]: j+=1
    if i>sums[j]:
        sum += i 
        j+=1

print(sum)
'''
