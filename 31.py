vals = [1,2,5,10,20,50,100,200]

combination = []
combinations = []

def looper(num, gap):
	if (num%gap==0):
		combination.append(num // gap)
		#return [true, num // gap]
	else:
		foo = num // gap
		if (num!=vals[0])
			looper(vals[vals.find(num)-1], gap-num*foo)

def alsoloop(num, gap):
	i = 1
	while (i*num <= gap):
		
		i = i + 1
		
	