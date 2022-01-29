from itertools import permutations
from itertools import combinations

def areSame(i, j):
    i.sort()
    j.sort()
    print(i, "::", j)
    return (i == j)

diffs = []
coins = 7


def getDiff(i):
    return [i[0], i[1]-i[0], i[2]-i[1], 7-i[2]]

def inn(i):
    global diffs
    newDiff = getDiff(i)
    for d in diffs:
        if areSame(newDiff,d):
            return True
    return False


def hacking():
    ctr = 0
    foo = []
    global diffs
    x = combinations([1,2,3,4,5,6],3)
    for i in x:
        i = list(i)
        ctr += 1
        print(i)
        if not inn(i):
            foo.append(i)
            diffs.append(getDiff(i))
    print(ctr)
    print("\n\n")
    print(foo)
    print("\n\n")
    for i in diffs:
        i.sort()
    print(diffs)

def testing():
    print(areSame([1,2,3], [3,2,1]))

hacking()
