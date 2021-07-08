'''
number has 1 => must be > 1           => number >= 1 digits
number has 2 => must be > 2           => number >= 1 digits
number has 3 => must be > 6           => number >= 1 digits
number has 4 => must be > 24          => number >= 2 digits
number has 5 => must be > 120         => number >= 3 digits
number has 6 => must be > 720         => number >= 3 digits
number has 7 => must be > 5040        => number >= 4 digits
number has 8 => must be > 40320       => number >= 5 digits
number has 9 => must be > 362880      => number >= 6 digits


<number of digits> - [possible digits in the number]:
        2          -            [0,1,2,3,4]                - [3,4]
        3          -            [0,1,2,3,4,5,6]            - [5,6]
        4          -            [0,1,2,3,4,5,6,7]          - [6,7]
        5          -            [0,1,2,3,4,5,6,7,8]        - [7,8]
        6,7        -            [0,1,2,3,4,5,6,7,8,9]      - [8,9], [9]

observation: you cannot have more than 8 digits in solution;
since the (best case) sum of factorial of digits is 7 digited
'''

from math import factorial

factorials = []
for i in range (10):
    factorials.append(factorial(i))
    # print(factorials[-1])

digits = ([0,1,2,3,4],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9])

solutions = []

def number_check_pt1(number):
    foo = str(number)
    if number < 100:
        if foo.count('3') == 0 and foo.count('4') == 0:
            return
        check(number,2)

    elif number < 1000:
        if foo.count('5') == 0 and foo.count('6') == 0:
            return
        check(number,3)

    elif number < 10000:
        if foo.count('6') == 0 and foo.count('7') == 0:
            return
        check(number,4)

    elif number < 100000:
        if foo.count('7') == 0 and foo.count('8') == 0:
            return
        check(number,5)

    #the 6 digit case
    elif number < 1000000:
        if foo.count('8') == 0 and foo.count('9') == 0:
            return
        check(number,6)

    else:
        if foo.count('9') == 0:
            return
        check(number,7)

#end of number_check_pt1

def check(number, size):
    sum = 0
    copy = number
    for i in range(size):
        sum = sum + factorials[number%10]
        number = number // 10
    if sum == copy:
        solutions.append(copy)

def ignition():
    for i in range (13,100):
        number_check_pt1(i)

    for i in range (121,1000):
        number_check_pt1(i)

    for i in range (1001,10000):
        number_check_pt1(i)

    for i in range (10001,100000):
        number_check_pt1(i)

    for i in range (100001,1000000):
        number_check_pt1(i)

    for i in range (1000001,10000000):
        number_check_pt1(i)

ignition()
print(solutions)
print(len(solutions))
