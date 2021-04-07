len = 0
starter_1 = [3,3,5,4,4,3,5,5,4] #1 thru 9
starter_2 = [6,6,8,8,7,7,9,8,8] # 11 thru 19
teners =    [3,6,6,5,5,5,7,6,6,7] #10 thru 100

for i, j in enumerate(starter_1): #the last word of each number ending with 1-9 (except the 11-19)
    if i>0 and i<9: len += 9*10* (i+teners[i]) #81

for i in teners: #the last word of each number whuch is a multiple of 10
    len += 1*10*i #10
len -= 7 #the thousand
len += 8 #the thousand

for i in starter_2: #last wrod of each number of type _1(1-9)
    len += 1*10*i #9

for i in starter_1: #the remaining words for nos >= 100 ()
    len += 99*9*(i+10)

for i in starter_1: #the 1st word of the 100's
    len += i

len += 3 #'one' thousand

print(len)