leap = False
days = 365
extra = 1
i = 1700 #test
start_days = [1] #run from sun to sat 0 - 6; this is as of 1 jan 1900
month_days = [31,28,31,30,31,30,31,30,31,31,30,31]
'''
for y in range(1900,1999):
	if ((y%4==0 and y%100!=0) or y%400==0):
		leap = True
		days = 366
		extra = 2
	else:
		leap = False
		days = 365	
		extra = 1
	print(y," : ", leap)	
	start_days.append((start_days[-1]+extra)%7)
'''

for y in range(1900,2000):
	if ((y%4==0 and y%100!=0) or y%400==0):
		month_days[1] = 29
	else:
		month_days[1] = 28
	for m in month_days:
		start_days.append((start_days[-1]%7+m)%7)

#print(start_days)
print(start_days.count(0))