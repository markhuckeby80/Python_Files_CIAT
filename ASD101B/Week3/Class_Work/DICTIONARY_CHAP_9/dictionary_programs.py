# Pg. 482 Program 8-2

import random


deck = {
    'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, 
    '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10, 
    'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10
    }


def deal_cards(deck, number):
    hand_value = 0
    
    if number > len(deck):
        number = len(deck)

    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        # hand_value += deck[card]
        hand_value += deck.pop(card)

    print(f'Value of this hand: {hand_value}')


if __name__ == '__main__':
    deal_cards(deck, random.randint(1, 13))