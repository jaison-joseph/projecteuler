from decimal import *

size = 100
getcontext().prec = size

def length(decimal):
	#print(decimal)
	count = 0
	'''
	count = decimal.count(decimal[0])
	if (count == len(decimal)):
		#print("recurr")
		return 0
	'''
	tmp = 0
	for i in range (1,size // 2):
		#print("not yet, ", decimal[0:i], "| count: ", decimal.count(decimal[0:i]))
		tmp = decimal.count(decimal[0:i])
		if (tmp < count):
			#print("found a drop")
			#print(decimal[0:i-1])
			return i-1
	return 0

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
	foo = str(Decimal(1)/Decimal(foofoo(i)))[2:]
	tmp = length(foo)
	if(tmp>max):
		max = tmp
		maxnum = foofoo(i)
'''

for i in range (1,499):
	foo = str(Decimal(1)/Decimal(2*i+1))[2:]
	tmp = length(foo)
	if(tmp>max):
		max = tmp
		maxnum = foofoo(i)
	'''
	for k in range (2):
		if (foo[0] == '0'):
			foo = foo[1:]
			tmp = length(foo)
			if(tmp>max):
				max = tmp
	'''
print("max length: ", max, " | divisor: ", maxnum)