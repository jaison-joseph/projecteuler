current = 3
combo = [(2,), (1,1,)]     # the  set of combinations

upper = 10
'''
so the inner loop should have been
combos += 1     # for the single element, (current)
combos += current // 2 - 1      # for the (current - i, i), 2 <= i <= current // 2 combos
'''

def advance(combo):
    global current
    new_ones = []
    for c in combo:
        uniq = [c.index(a) for a in set(c)]
        for i in uniq:
            c[i] += 1
            # print(tuple(c))
            new_ones.append(tuple(c))
            c[i] -= 1
    list(map(lambda x: x.append(1), combo))
    combo = list(set(new_ones))
    combo.append(tuple([1]*current))
    return combo

def test():
    test_cases = [[[1]], [[2],[1,1]], [[3],[2,1], [1,1,1]], [[4], [3,1], [2,2], [1,1,1,1], [2,1,1]]]
    for index, t in enumerate(test_cases):
        print(index+2, ":", t, " || ", advance(t))
        print("\n\n")

def run():
    global current, upper, combo
    new_ones = []
    while len(combo) % 10**6 != 0:
        new_ones = []
        combo = list(map(list, combo))
        for c in combo:
            uniq = [c.index(a) for a in set(c)]
            # print("uniq:", uniq," | combo:", c)
            for i in uniq:
                c[i]+=1
                # print("c:", c)
                new_ones.append(c[:])
                # print("new_ones:", new_ones)
                c[i]-=1
        # print("\n\n", combo," :: ", new_ones)
        list(map(lambda x: x.append(1), combo))
        combo += new_ones
        combo = list(map(tuple, combo))
        combo = list(set(combo))
        current += 1
    print(current, " :: ", len(combo))

try:
    run()
except:
    print("current:", current)
    print("combo:", len(combo))

# while current < upper:
#     to_add = []
#     combos.append([current])
#     for c in combos:
#
#     print(current, ":", combos)
#     current += 1
