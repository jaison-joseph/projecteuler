start = 1
sum = 1
for i in range(2,2*501,2):
	for j in range (1,5):
		start = start+i
		sum = sum + start	

print(sum)