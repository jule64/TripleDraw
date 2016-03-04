
'''
Some utility methods to convert cards to integer values
and so on
'''


def convert_cards_to_integers(starting_hand, deck):
    return [deck.cards_to_int_dict[j] for j in starting_hand]

def convert_integer_cards_to_cards(retained_integer_cards, deck):
    return [deck.int_to_cards_dict[j] for j in retained_integer_cards]
