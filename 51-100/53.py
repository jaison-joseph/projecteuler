# does nCr (partially)
# returns True if at any stage of computong result, the value > 10**6
# returns False otherwise

upper = 10**6
def combos(n, r):
    global upper
    numerator = [i for i in range(2, n+1)]
    denominator = [i for i in range(2, r+1)]
    for i in range(2, n-r+1):
        denominator.append(i)
    # print("n:", n)
    # print("r:", r)
    # print("numerator:", numerator)
    # print("denominator:", denominator)
    i = 0
    foo = 0
    while i < len(denominator):
        foo = denominator[i]
        if foo in numerator:
            numerator.remove(foo)
            denominator.remove(foo)
        else:
            i += 1
    i = 0
    prod = 1
    while i < len(numerator):
        prod *= numerator[i]
        if i < len(denominator):
            prod /= denominator[i]
        else:
            if prod > upper:
                return True
        i += 1
    # print("numerator:", numerator)
    # print("denominator:", denominator)
    return False

solutions = 0

for n in range(1,101):
    for r in range(1,n):
        if combos(n,r):
            solutions += 1

print(solutions)
