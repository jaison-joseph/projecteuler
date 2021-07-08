num = 1
while True:
    x = set(str(num))
    if x == set(str(num*2)):
        if x == set(str(num*3)):
            if x == set(str(num*4)):
                if x == set(str(num*5)):
                    if x == set(str(num*6)):
                        print("solution is: ", num)
                        exit(0)
    num += 1
