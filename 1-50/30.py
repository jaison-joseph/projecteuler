nos = []

def nice(num):
	copy = num
	foo = 0
	while (num>0):
		foo = foo + (num%10)**5
		num = num // 10
		if (foo > copy):
			return False	
	if (copy == foo):
		return True
	else:
		return False



for num in range(10,354295):
	if nice(num):
		nos.append(num)


print(sum(nos))	
print(nos)	
#print(nice(1634))