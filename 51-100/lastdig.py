def lastdig(num):
    if type(num) is not int:
        raise TypeError
    return num%10
#
# print(lastdig(1))
# print(lastdig(123))

def consecPrime():
    nos = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
    last = nos[-1]
    diff = [set(str(last - i)) for i in nos[:-1]]
    foo = set([len(set(str(last - i))) for i in nos[:-1]])
    lengths = [len(x) for x in diff]
    print(diff)
    print(lengths)
    print(foo)

consecPrime()

def foo():
    x = [i for i in range(1,21)]
    print(x)
    for i in range(8,len(x)):
        last = x[i]
        print(i, "::",last, "::", x[i-8:i])

# foo()
