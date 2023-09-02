import random
# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        hand_value += deck.pop(card)

    # Display the value of the hand.
    print(f'Value of this hand: {hand_value}')