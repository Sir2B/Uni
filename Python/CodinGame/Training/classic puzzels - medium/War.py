import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cards = "2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A".split(", ")
suits = "D, H, C, S".split(", ")

cards_p1 = []
cards_p2 = []
n = int(raw_input())  # the number of cards for player 1
for _ in xrange(n):
    cardp_1 = raw_input()  # the n cards of player 1
    cards_p1.append(cardp_1[:-1])
m = int(raw_input())  # the number of cards for player 2
for _i in xrange(m):
    cardp_2 = raw_input()  # the m cards of player 2
    cards_p2.append(cardp_2[:-1])


def get_value_of_card(card):
    global cards
    return cards.index(card)


def war(card_p1, card_p2):
    global cards_p1, cards_p2
    war_running = True
    war_cards_p1 = [card_p1]
    war_cards_p2 = [card_p2]
    while war_running:
        if len(cards_p1) < 4 or len(cards_p2) < 4:
            cards_p1[:] = []
            cards_p2[:] = []
            return
        for _ in xrange(3):
            war_cards_p1.append(cards_p1.pop(0))
            war_cards_p2.append(cards_p2.pop(0))
        card1 = cards_p1.pop(0)
        card2 = cards_p2.pop(0)
        war_cards_p1.append(card1)
        war_cards_p2.append(card2)
        value1 = get_value_of_card(card1)
        value2 = get_value_of_card(card2)
        if value1 != value2:
            war_running = False
    war_winner = cards_p2 if value1 < value2 else cards_p1
    war_winner.extend(war_cards_p1)
    war_winner.extend(war_cards_p2)


rounds = 0
while len(cards_p1) != 0 and len(cards_p2) != 0:
    rounds += 1
    card_p1 = cards_p1.pop(0)
    card_p2 = cards_p2.pop(0)
    if get_value_of_card(card_p1) < get_value_of_card(card_p2):
        winner = cards_p2
    elif get_value_of_card(card_p1) > get_value_of_card(card_p2):
        winner = cards_p1
    else:
        war(card_p1, card_p1)
        continue
    winner.append(card_p1)
    winner.append(card_p2)

if len(cards_p1) == 0 and len(card_p2) == 0:
    print "PAT"
else:
    winner = 2 if len(cards_p1) == 0 else 1
    print "{0} {1}".format(winner, rounds)
