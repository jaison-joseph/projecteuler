# from sys import exit
from math import sqrt

def getHex(num):
    return num*(2*num-1)

def isPent(num):
    num = 24*num+1
    sr = int(sqrt(num))
    if sr*sr == num:
        if sr%6 == 5:
            return True
    return False

def isTri(num):
    num = 8*num + 1
    sr = int(sqrt(num))
    if sr*sr == num:
        if sr%2 == 1:
            return True
    return False

i = 144
while True:
    num = getHex(i)
    if isPent(num) and isTri(num):
        print(num)
        break
    i += 1
