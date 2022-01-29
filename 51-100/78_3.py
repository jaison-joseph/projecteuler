'''
this is a clean illustration of the idea I will use for the final version
the difference will be that combos will simply contain the previous result
'''

import pprint

prevCombo = 3
hi = 0
lo = 0
# this method was designed with the assumption that 
# the input > 4

def getCombo(num):
    prevCombo += 1
    
    while hi >= lo:
        prevCombo += 1
        hi -= 1
        lo += 1

if __name__ == "__main__":
    sed = 4
    while prevCombo % 10**6 != 0:
        prevCombo += 1
        hi = sed-2
        lo = 2
        while hi >= lo:
            prevCombo += 1
            hi -= 1
            lo += 1
        sed += 1
    print("\n the solution is:", sed)
        # pprint.pprint(prevCombo)
