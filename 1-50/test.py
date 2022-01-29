from decimal import *

longest = 0
num = 0

getcontext().prec = 200

def pattern(no):
    alsoNo = no
    #print("Original no: ", no)
    no = str(no)
    pattern = ''
    no = no[no.find('.')+1:]
    l = 0
    for j in no:
        #print("No: ", no, "|| Pattern: ", pattern)
        pattern += j
        #print(i, ", ", j)
        no = no[1:]
        for i in range (5):
            if (pattern[i:] == no[:len(pattern-i)] and len(pattern)>3):
                l = len(pattern)-i
                return 
        if (len(pattern)>100): break
    
    global longest
    if (l>longest): 
        longest = l
        global num
        num = alsoNo

    #if l == 0:
    #    print("for ", alsoNo, ", no pattern found")
    #else:
    #    print("for ", alsoNo, ", pattern is; ", pattern)


for i in range(3,1000):
    pattern(Decimal(1)/Decimal(i))

print(longest, ": ", num**-1)


#print(Decimal(1)/Decimal(793))
#pattern(Decimal(1)/Decimal(793))