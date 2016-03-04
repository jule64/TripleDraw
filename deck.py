'''
Created on Mar 26, 2013

@author: jule64@gmail.com

Instantiates a deck of cards and provides methods for accessing
those cards.

The main deck list is ordered on ranks and suits as follow:
['2c', '3c', 'Qc',...,'3d', '4d', ..., '10h', 'Jh', ..., 'Ks', 'As']

Important: !!Semantic dependencies!!
Classes such as CardRules are dependent on how the cards are ordered in
the deck in this class.  Hence you should NOT change the current order
of cards in the deck or it will create unpredictable behaviour in those
external classes that depend on that order being as it currently is.
'''


import random
import re

class Deck(object):



    def __init__(self):
        '''
        Initialising data structures
        '''

        self.colors = ['s','c','d','h']
        self.ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

        # create list of all cards sorted by color and rank
        # ['2c', '3c',...,'Kc',...,'As']
        self.cards=[i + j for i, j in zip(self.ranks * 4, sorted(self.colors * 13))]
        
        # create dict of cards mapped to an integer key, in sorted order
        # {0: '2c', 1: '3c', 2: '4c',...}
        self.int_to_cards_dict = dict(enumerate(self.cards))

        # reverse mapp the all_cards_dict to  create a dict of cards mapped to integer
        # {'9h': 33, '10h': 34,...}
        # note we don't need to sort the  resulting dict
        self.cards_to_int_dict={}
        for item in self.int_to_cards_dict.iteritems():
            self.cards_to_int_dict[item[1]]=item[0]

        # shuffle main deck
        # random.shuffle(self.cards)
        
        #the below results in dict of ranks only:
        #{'A': 12, '10': 8, 'K': 11, 'J': 9, 'Q': 10, ...}
        self.rankstonum = [(j,i) for i,j in enumerate(self.ranks)]
        self.rankstonum_dict = dict(self.rankstonum)

        self._deck=[]


    def get_card(self):
        '''
        Retrieves a random card from the deck
        :return: card
        '''
        # TODO based on profiler results, random number generation take up about 20% of
        # runtime.  One way to optimise could be to create some kind of random number service that
        # runs in its own process and specialises in providing random numbers to worker processes.
        # Perhaps that would speed up calculations
        cardIndex=int(random.random()*len(self.cards))
        return self.cards.pop(cardIndex)

    def remove_card_from_deck(self, c):
        try:
            self.cards.remove(c)
        except:
            raise Exception("the card <{}> does not exists.  Please check your starting cards".format(c))

    def convert_rank_to_int(self, rank):
        # TODO handle exception when rank is incorrect
        return self.ranks.index(rank)






        
    
    
        