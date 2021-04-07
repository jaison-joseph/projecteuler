x = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

print(x[1018])
print(len(x))

#run a for loop until the last character in x
#select thirteen characters at a time using slicing and the var posn of end
#see if 0 is there
#   if yes, then pass, 
#   else, ake their prod, compare to biggest, update prod AND end_of_biggest if grater
#increment position of end, close while loop

#lengths = []
#anti_number = 0

position_of_end = 12
end_of_biggest = 12
biggest_prod = 0

while position_of_end < 1019:
    selection = list(x[position_of_end - 12 : position_of_end + 1])
    all_good = True
    for smth in selection:
        if not smth.isdigit():
            selection.remove('\n')
            position_of_end += 1
            selection.append(x[position_of_end + 1])
    for another in selection:    
        if another is '0': 
            all_good = False
   
    if all_good is True:
        prod = 1
        for varr in selection:
            prod *= int(varr)
        if prod > biggest_prod:
            biggest_prod = prod
            end_of_biggest = position_of_end
    position_of_end += 1

print("Biggest product is: {}".format(biggest_prod))
print("Biggest product's position is: {}".format(end_of_biggest))



final_dest = list(x[end_of_biggest - 12 : end_of_biggest + 1])
print(final_dest)
'''
prod = 1
for smth in final_dest:
    try:   prod *= int(smth)
    except: final_dest.append(list(x[end_of_biggest+1]))
print(prod)
'''
