# imports
from operator import itemgetter

# this will contain 1000 lists, each list, containing 2 lists of hands 
l = []

# the 2 - 10, then J Q K A
values = [str(i) for i in range(2,10)]
values.append('T') #T for ten
values.append('J')
values.append('Q')
values.append('K')
values.append('A')

consecutive_face_values = []
for j in range(0,13):
    consecutive_face_values.append(sorted(
        [values[k%13] for k in range(j,j+5)], 
        key = lambda x: values.index(x)
    ))

royal_flush_values = ['T', 'J', 'Q', 'K', 'A']


# accepts a pair of hands, spits out a winner
def winner(hands):
    global royal_flush_values, consecutive_face_values, values
    
    # h1 -> the hand of player 1
    # h2 -> the hand of player 2
    # h2_v -> the values (ace, 7, 4) of p2's cards
    # h2_v -> the faces (spade, club) of p2's cards
    
    h1 = hands[0]
    h1_v = [i[0] for i in h1]
    h1_f = [i[1] for i in h1]
    h2 = hands[1]
    h2_v = [i[0] for i in h2]
    h2_f = [i[1] for i in h2]

    # will be changed to 1 or 2
    winner = -1

    # the levels of comparisons, starting from royal flush and ending in highest card
    level = 10
    
    if winner == -1:
        level = 10    
        v1 = h1_v[:]
        f1 = h1_f[:] 
        v1 = sorted(v1, key = lambda x: values.index(x))
        v2 = h2_v[:]
        f2 = h2_f[:] 
        v2 = sorted(v2, key = lambda x: values.index(x))
        if f1.count(f1[0]) == 5 and v1 == royal_flush_values:
            winner = 1
        if f2.count(f2[0]) == 5 and v2 == royal_flush_values:
            # we have a tie 
            if winner != -1:
                winner = -1
            else:
                winner = 2 
    
    if winner == -1:
        level = 9
        v1 = h1_v[:]
        f1 = h1_f[:] 
        v1 = sorted(v1, key = lambda x: values.index(x))
        v2 = h2_v[:]
        f2 = h2_f[:] 
        v2 = sorted(v2, key = lambda x: values.index(x))
        
        if f1.count(f1[0]) == 5 and v1 in consecutive_face_values:
            winner = 1
        if f2.count(f2[0]) == 5 and v2 in consecutive_face_values:
            # we have a tie 
            if winner != -1:
                # better face values can break the tie
                s1 = sum(list(map(lambda x: values.index(x), v1)))
                s2 = sum(list(map(lambda x: values.index(x), v2)))
                if s1 > s2:
                    winner = 1
                elif s1 < s2:
                    winner = 2
                else:
                    winner -= 1
            else:
                winner = 2

    if winner == -1:
        level = 8
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:] 

        if v1.count(v1[0]) == 4 or v1.count(v1[1]) == 4:
            winner = 1
        if v2.count(v2[0]) == 4 or v2.count(v2[1]) == 4:
            if winner != -1:
                best_1 = v1[0] if v1.count(v1[0]) == 4 else v1[1]
                best_2 = v2[0] if v1.count(v2[0]) == 4 else v2[1]
                best_1 = values.index(best_1)
                best_2 = values.index(best_2)
                if best_1 > best_2:
                    winner = 1
                elif best_1 < best_2:
                    winner = 2
                else:
                    winner = -1
            else:
                winner = 2

    if winner == -1:
        level = 7
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:]

        # we know that if the result is either a 3 2 or a 4 1
        # since level 8 is four of a kind and that was checked earlier, 4 1 is ruled out
        # that means if the length of the set is 2, it is a 3 2
        if len(set(v1)) == 2:
            winner = 1
        if len(set(v2)) == 2:
            if winner != -1:
                x1 = [[values.index(i), v1.count(i)] for i in set(v1)]
                x2 = [[values.index(i), v2.count(i)] for i in set(v2)]
                x1 = sorted(x1, key = itemgetter(1), reverse=True)
                x2 = sorted(x2, key = itemgetter(1), reverse=True)
                for i, j in zip(x1, x2):
                    if i[0] > j[0]:
                        winner = 1
                        break
                    elif i[0] < j[0]:
                        winner = 2
                        break
                if winner == -1:
                    pass
            else:
                winner = 2

    if winner == -1:
        level = 6
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:]

        if len(set(f1)) == 1:
            winner = 1
        if len(set(f2)) == 1:
            if winner != -1:
                winner = -1
            else:
                winner = 2

    if winner == -1:
        level = 5
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:]

        v1 = sorted(v1, key = lambda x: values.index(x))
        v2 = sorted(v2, key = lambda x: values.index(x))

        if v1 in consecutive_face_values:
            winner = 1
        if v2 in consecutive_face_values:
            if winner != -1:
                for i, j in zip(v1[::-1], v2[::-1]):
                    if i > j:
                        winner = 1
                        break
                    if i < j:
                        winner = 2
                        break
                if winner == -1:
                    pass
            else:
                winner = 2 
        
    if winner == -1:
        level = 4
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:]

        if 3 in list(map(lambda x: v1.count(x), v1)):
            winner = 1
        if 3 in list(map(lambda x: v2.count(x), v2)):
            if winner != -1:
                p1 = v1[0] if v1.count(v1[0]) == 3 else v1[1] if v1.count(v1[1]) == 3 else v1[2]
                p2 = v2[0] if v1.count(v2[0]) == 3 else v2[1] if v1.count(v2[1]) == 3 else v2[2]
                p1 = values.index(p1)
                p2 = values.index(p2)
                if p1 > p2:
                    winner = 1
                elif p2 < p2:
                    winner = 2
                else:
                    winner = -1
            else:
                winner = 2

    if winner == -1:
        level = 3
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:]

        v1 = dict((i, v1.count(i)) for i in set(v1))
        v2 = dict((i, v2.count(i)) for i in set(v2))

        if list(v1.values()).count(2) == 2:
            winner = 1
        if list(v2.values()).count(2) == 2:
            if winner != -1:
                p1 = [i for i,j in v1.items() if j == 2]
                p2 = [i for i,j in v2.items() if j == 2]
                p1.sort(reverse=True)
                p2.sort(reverse=True)
                for i, j in zip(p1, p2):
                    if i > j:
                        winner = 1
                        break
                    if i < j:
                        winner = 2
                        break
                if winner == -1:
                    pass 
            else:
                winner = 2
    
    if winner == -1:
        level = 2
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:]

        v1 = dict((i, v1.count(i)) for i in set(v1))
        v2 = dict((i, v2.count(i)) for i in set(v2))

        if 2 in v1.values():
            winner = 1
        if 2 in v2.values():
            if winner != -1:
                p1 = [i for i, j in v1.items() if j == 2][0]
                p2 = [i for i, j in v2.items() if j == 2][0]
                p1 = values.index(p1)
                p2 = values.index(p2)
                if p1 > p2:
                    winner = 1
                elif p1 < p2:
                    winner = 2
                else:
                    winner = -1
            else:
                winner = 2
            
    if winner == -1:
        level = 1
        v1 = h1_v[:]
        f1 = h1_f[:] 
        
        v2 = h2_v[:]
        f2 = h2_f[:]

        v1 = list(map(lambda x: values.index(x), v1))
        v2 = list(map(lambda x: values.index(x), v2))

        v1.sort(reverse=True)
        v2.sort(reverse=True)

        for i, j in zip(v1, v2):
            if i > j:
                winner = 1
                break
            if i < j:
                winner = 2
                break
        
        if winner == -1:
            print("what the duck is happening!")
            exit(0)

    return [winner, level]


def master():

    global l 

    #file reading
    with open("poker.txt") as f:
        l = f.readlines()
        l = [[i[:14].split(' '), i[15:-1].split(' ')] for i in l]

    score = {}
    score[1] = 0
    score[2] = 0

    for i, round in enumerate(l):
        score[winner(round)[0]] += 1
        # try:
        #     score[winner(round)] += 1
        # except Exception as e:
        #     print(e.__dict__)
        #     print(i, "::", round)
        #     exit(0)

    print(score)


def test():
    pairs = [
        [["5H", "5C", "6S", "7S", "KD"], ["2C", "3S" ,"8S" ,"8D" ,"TD"]],
        [["5D", "8C", "9S", "JS", "AC"], ["2C", "5C" ,"7D" ,"8S" ,"QH"]],
        [["2D", "9C", "4S", "AH", "AC"], ["3D", "3S" ,"7D" ,"7C" ,"QD"]],
        [["QH", "KH", "JH", "2C", "AH"], ["3C", "3D" ,"3S" ,"9S" ,"TD"]],
        [["QH", "KH", "JH", "TH", "AH"], ["3C", "3D" ,"3S" ,"9S" ,"9D"]],
        [["QH", "KH", "JH", "2H", "AH"], ["3C", "3D" ,"3S" ,"9S" ,"9D"]],
        [["QH", "KH", "JH", "TC", "AH"], ["2D", "3D" ,"4D" ,"9D" ,"TD"]],
        [["QH", "5C", "JD", "3S", "AH"], ["3C", "3D" ,"3S" ,"9S" ,"7D"]],
        [["3C", "3D" ,"3S" ,"AS" ,"7D"], ["3C", "3D" ,"3S" ,"9S" ,"7D"]],
        [["2D", "2D", "4D", "4D", "4D"], ["3C", "3D" ,"3S" ,"9S" ,"9D"]],
        [["2H", "2D", "4C", "4D", "4S"], ["3C", "3D" ,"3S" ,"3H" ,"9D"]]
    ]

    for i, p in enumerate(pairs): 
        r = winner(p)
        print(r[1], "::", r[0])

    global consecutive_face_values
    # list(map(print, consecutive_face_values))
    print(consecutive_face_values)

# test()
master()
