import inspect

denominations = [1,2,5,10,20,50,100,200]
#denominations = [20,50,100,200]

combinations = []

ct = 0

max_amount = 200 

def add_one(current, ind):
    global ct, total
    ct+=1
    for index, i in enumerate(denominations[ind:]):
        total = sum(current) + i
        if total < max_amount:
            temp = current[:]
            temp.append(i)
            add_one(temp, index+ind)
        elif total == max_amount:
            current.append(i)
            combinations.append(current)
            return
        else:
            return

for index, i in enumerate(denominations):
    temp = [i]
    add_one(temp, index)

print("\n The total count is: ",len(combinations))
print("\n ct is: ", ct)
