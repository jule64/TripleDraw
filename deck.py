import random

class Deck(object):
    """Instantiates a deck of cards and provides methods for accessing
    those cards.

    The main deck/stack list is ordered on ranks and suits as follow:
    ['2c', '3c', 'Qc',...,'3d', '4d', ..., '10h', 'Jh', ..., 'Ks', 'As']
    """

    def __init__(self):
        """Initialising data structures"""

        self.colors = ['s','c','d','h']
        self.ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

        # create a list of 52 cards sorted by rank and suit (color).  The list will
        # always be ordered like so: clubs> diamonds > hearts > spades
        # ['2c','3c', '4c',.,'Jd',..,'8h'..., 'Ks', 'As']
        #
        # Note for performance reasons the list is generated only once and
        # public methods access a copy of it named `cards`. See `initialise()`
        self.__template_card_stack = [i + j for i, j in zip(self.ranks * 4, sorted(self.colors * 13))]

        # create dict of cards mapped to an integer key, in sorted order
        # {0: '2c', 1: '3c', 2: '4c',...}
        self.int_to_cards_dict = dict(enumerate(self.__template_card_stack))

        # create a dict of cards to integer based on the order of the template stack
        # {'9h': 33, '10h': 34,...}
        # note we don't need to sort the  resulting dict
        self.cards_to_int_dict=dict([(j,i) for i,j in enumerate(self.__template_card_stack)])

    def initialise(self):
        """Creates a new stack of 52 cards
        :return: void
        """
        # note for performance reasons we copy the main cards list instead of re-creating
        # a new list from scratch
        self.card_stack= self.__template_card_stack[:]

    def get_card(self):
        """Retrieves a card randomly from the deck.  This is equivalent to retrieving
        a card from a shuffled deck but is faster since only the needed cards are shuffled
        not the whole deck.
        :return: card
        """
        # TODO based on profiler results, random number generation take up about 20% of
        # runtime.  One way to optimise could be to create some kind of random number service that
        # runs in its own process and specialises in providing random numbers to worker processes.
        # Perhaps that would speed up calculations
        card_index=int(random.random() * len(self.card_stack))
        return self.card_stack.pop(card_index)

    def remove_card_from_deck(self, c):
        try:
            self.card_stack.remove(c)
        except:
            raise Exception("the card <{}> does not exists".format(c))




        
    
    
        