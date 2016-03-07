
'''Some utility methods to convert cards to and from
integer values
'''

def convert_cards_to_integers(starting_hand, deck):
    return [deck.cards_to_int_dict[j] for j in starting_hand]

def convert_integer_cards_to_cards(retained_integer_cards, deck):
    return [deck.int_to_cards_dict[j] for j in retained_integer_cards]

def convert_rank_to_int(rank,deck):
    # TODO handle exception when rank is incorrect
    return deck.ranks.index(rank)


def is_high_card(hand,target):
    return max(x%13 for x in hand)>target

def is_straight(hand):
    def f(x,y):
        if x[0] is None:
            x[0]=y
            return x
        if(x[1] is True and y%13-x[0]%13==1):
            x[0]=y
            return x
        x[1]=False
        return x
    return reduce(f,hand,[None,True])[1]


def is_flush(hand):
    def f(x,y):
        if x[0] is None:
            x[0]=y
            return x
        if(x[1] is True and y/12==x[0]/12):
            x[0]=y
            return x
        x[1]=False
        return x
    return reduce(f,hand,[None,True])[1]

def is_pair(hand):
    def f(x,y):
        if x[0] is None:
            x[0]=y
            return x
        elif x[1] is False and y%13==x[0]%13:
                x[0]=y
                x[1]=True
                return x
        x[0]=y
        return x
    return reduce(f,hand,[None,False])[1]

