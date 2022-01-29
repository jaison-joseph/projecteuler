#the below script is the actual solution

def uselesstriangle():
    triangle_slices = [[1], [1,1]]

    for i in range(2,10):
        prev = triangle_slices[-1]
        pt1 = [0]+prev
        pt2 = prev+[0]
        triangle_slices.append([(pt1[x]+pt2[x]) for x in range(i+1)])

prev_pows = []
prec = 11
def mult(n1, n2):
    global prec
    # print("expected answer: ", n1*n2)
    sum = 0
    n1_s = str(n1)[-prec:]
    n2_s = str(n2)[-prec:]
    for index, dig in enumerate(n2_s[::-1]):
        # print(n1_s[:prec-index], "::", dig+'0'*index)
        #len(dig+'0'*index)-11
        # sum += int(n1_s[:prec-index]) * int(dig+'0'*index)
        sum += int(n1_s[len(dig+'0'*index)-prec:]) * int(dig+'0'*index)
    # print(str(sum)[-10:] == str(n1**n2)[-1*len(str(sum)[-10:]):])
    return int(str(sum)[-10:])

def myPow(num, pow):
    prod = 1
    for i in range(pow):
        prod = mult(prod,num)
    return prod

def test():
    num = 118
    x = myPow(num,num)
    y = str(num**num)[-10:]
    print(x)
    print(y)
    print(str(x) == y)

modulo_number = 10**10

def ignition():
    global modulo_number
    sum = 0
    for i in range(1,1001):
        sum += myPow(i,i)
        sum %= modulo_number
    print(sum)

ignition()
# test()
