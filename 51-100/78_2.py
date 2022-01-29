'''
this is a clean illustration of the idea I will use for the final version
the difference will be that combos will simply contain the previous result
'''

import pprint

combos = dict()

combos[2] = [[2], [1,1]]
combos[3] = [[3], [2,1], [1,1,1]]

# this method was designed with the assumption that 
# the input > 4

strapOn = lambda b,extra:b.append(extra)

def getCombo(num):
    temp = []
    temp.append([num])
    hi = num-1
    lo = 1
    temp += [c+[lo] for c in combos[hi]] 
    hi -= 1
    lo += 1
    while hi >= lo:
        temp.append([hi,lo])
        hi -= 1
        lo += 1
    combos[num] = temp

if __name__ == "__main__":
    seeds = [i for i in range(4,6)]
    for sed in seeds:
        getCombo(sed)
    pprint.pprint(combos)
