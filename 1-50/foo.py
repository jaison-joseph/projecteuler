from decimal import *
import pdb; pdb.set_trace()
size = 100
getcontext().prec = size + 2

def length(decimal):
	print(decimal, " : " ,decimal[0])
	splits = decimal.split(decimal[0])
	#print(decimal, " : " ,splits)
	if (len(splits) == 2):
		return 0
	print(decimal[0]+splits[1])
	return (1+len(splits[1]))

#foo = str(Decimal(1)/Decimal(6))[2:]

max = -1
maxnum = 0
def poopoo(x): return 6*x+1
def foofoo(x): return 6*x-1

'''
for i in range(1,200):
	if (poopoo(i)>=1000): break
	foo = str(Decimal(1)/Decimal(poopoo(i)))[2:]
	tmp = length(foo)
	if(tmp>max):
		max = tmp
		maxnum = poopoo(i)

for i in range(1,200):
	if (foofoo(i)>=1000): break
	foo = str(Decimal(1)/Decimal(foofoo(i)))[2:-2]
	tmp = length(foo)
	if(tmp>max):
		max = tmp
		maxnum = foofoo(i)
'''
'''
for i in range (1,499):
	foo = str(Decimal(1)/Decimal(2*i+1))[2:-2]
	tmp = length(foo)
	if(tmp>max):
		max = tmp
		maxnum = foofoo(i)
	for k in range (2):
		if (foo[0] == '0'):
			foo = foo[1:]
			tmp = length(foo)
			if(tmp>max):
				max = tmp
'''
for i in range (1,1000//6+1):
	foo = str(Decimal(1)/Decimal(poopoo(i)))[2:-2]
	tmp = length(foo)

print("max length: ", max, " | divisor: ", maxnum)