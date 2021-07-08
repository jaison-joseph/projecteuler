# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# ascending values: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

import pprint
from itertools import permutations

p1 = []
p2 = []

stats = [0] * 10

values = [str(i) for i in range(2,10)]
values.append('T') #T for ten
values.append('J')
values.append('Q')
values.append('K')
values.append('A')

royal_flush_face_values = list(permutations(['T', 'J', 'Q', 'K', 'A']))

consecutive_face_values = []
for j in range(0,12):
    consecutive_face_values += list(permutations([values[k%13] for k in range(j,j+5)]))


def handValue(hand):
    global consecutive_face_values
    global royal_flush_face_values
    global values
    faceValues = [h[:-1] for h in hand]
    ranks = list(map(values.index, faceValues))
    suits = [h[-1] for h in hand]
    # if False:
    #     print("\nhand:", hand)
    #     print("faceValues:", faceValues)
    #     print("suits:", suits)

    points = []

    # royal Flush
    if faceValues in royal_flush_face_values and suits.count(suits[0]) == 5:
        points.append(10)
    if faceValues in consecutive_face_values and suits.count(suits[0]) == 5:
        points.append(9)
    if faceValues.count(faceValues[0]) == 5:
        points.append(8)
    if set(list(map(faceValues.count, faceValues))) == {2,3}:
        points.append(7)
    if suits.count(suits[0]) == 5:
        points.append(6)
    if faceValues in consecutive_face_values:
        points.append(5)

    occurences = list(map(faceValues.count, faceValues))
    if 3 in occurences:
        points.append(4)
    if occurences.count(2) == 4:
        points.append(3)
    if occurences.count(2) == 2 and occurences.count(1) == 3:
        points.append(2)
    points.append(1)

    return [points, ranks]


def get_winner_2(h1, h2):
    global stats, values
    r1 = handValue(h1)
    r2 = handValue(h2)
    for pt in r1[0]:
        stats[pt-1] += 1
    for pt in r2[0]:
        stats[pt-1] += 1
    try:
        while (max(r1[0]) == max(r2[0])):
            if max(r1[0]) ==
            r1[0].remove(max(r1[0]))
            r2[0].remove(max(r2[0]))
        if max(r1[0]) > max(r2[0]):
            return 0
        else:
            return 1
    except ValueError:
        if len(r1[0]) == 0:
            if len(r2[0]) == 0:

            return 1
        return 0


def get_winner(h1, h2):
    global stats, values
    r1 = handValue(h1)
    r2 = handValue(h2)
    stats[r1[0]-1] += 1
    stats[r2[0]-1] += 1
    # f = [r1[1][:], r2[1][:]]
    if r1[0] > r2[0]:
        return 0
    elif r1[0] < r2[0]:
        return 1
    else:
        r1 = r1[1][:]
        r2 = r2[1][:]
        try:
            while max(r1) == max(r2):
                r1.remove(max(r1))
                r2.remove(max(r2))
            if max(r1) > max(r2):
                return 0
            else:
                return 1
        except ValueError:
            f1 = [h[:-1] for h in h1]
            r1 = list(map(values.index, f1))
            f2 = [h[:-1] for h in h2]
            r2 = list(map(values.index, f2))
            print(h1, "::", r1)
            print(h2, "::", r2)
            exit(0)

f = open("p054_poker.txt")
for line in f:
    x = line.split(' ')
    p1.append(x[:5])
    p2.append(x[5:])
    p2[-1][-1] = p2[-1][-1][:-1]

f.close()

if (False):
    print("consecutives")
    pprint.pprint(consecutives)
    print("part of p1")
    pprint.pprint(p1[:20])
    print("part of p2")
    pprint.pprint(p2[:20])

#getting the scores

scores = [0,0]
for i in range(len(p1)):
    scores[get_winner_2(p1[i], p2[i])] += 1

print("scores: ", scores)
print("stats: ", stats)
print("len(consecutive_face_values): ", len(consecutive_face_values))
# card[-1] to get the suit
# card[:-1] to get the value
