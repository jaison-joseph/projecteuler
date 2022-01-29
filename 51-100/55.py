if True:
    count = 0
    for n in range(1, 10000):
        for i in range(49):
            n2 = str(n + int(str(n)[::-1]))
            # print(str(n) + " + " + str(n)[::-1] + " = " + n2)
            # print("n2; ", n2)
            if n2 == n2[::-1]:
                # print(str(n) + " + " + str(n)[::-1] + " = " + n2 + " we have a pallindrome")
                count += 1
                break
            n = int(n2)
        # print("---------------------")
    print("count: ", 10000 - count)

else:
    n = 23
    n2 = str(n + int(str(n)[::-1]))
    # print(str(n) + " + " + str(n)[::-1] + " = " + n2)
    print("n2; ", n2, ": ", n2 == n2[::-1])
