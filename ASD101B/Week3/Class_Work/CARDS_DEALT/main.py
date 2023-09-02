# This program uses a dictionary as a deck of cards.
from create_deck import create_deck
from deal_cards import deal_cards

def main():
    # Create a deck of cards.
    deck = create_deck()
    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))
    # Deal the cards.
    deal_cards(deck, num_cards)

# Call the main function.
if __name__ == '__main__':
    main()