'''
Created on Mar 26, 2013

@author: jule64@gmail.com



Sorted Deck Mapping:
{0: '2c', 1: '3c', 2: '4c', 3: '5c', 4: '6c', 5: '7c', 6: '8c', 7: '9c', 8: '10c'
, 9: 'Jc', 10: 'Qc', 11: 'Kc', 12: 'Ac', 13: '2d', 14: '3d', 15: '4d', 16: '5d'
, 17: '6d', 18: '7d', 19: '8d', 20: '9d', 21: '10d', 22: 'Jd', 23: 'Qd', 24: 'Kd'
, 25: 'Ad', 26: '2h', 27: '3h', 28: '4h', 29: '5h', 30: '6h', 31: '7h', 32: '8h'
, 33: '9h', 34: '10h', 35: 'Jh', 36: 'Qh', 37: 'Kh', 38: 'Ah', 39: '2s', 40: '3s'
, 41: '4s', 42: '5s', 43: '6s', 44: '7s', 45: '8s', 46: '9s', 47: '10s', 48: 'Js'
, 49: 'Qs', 50: 'Ks', 51: 'As'}

'''


import random
import warnings



class Deck(object):
    '''
    the deck gets initialised by calling get_sequences()
    
    '''


    def __init__(self):
        '''
        Initialises map structures
        '''
        
        self.suits = ["s","c","d","h"]
        self.ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.all_cards=[i+j for i,j in zip(self.ranks*4,sorted(self.suits*13))]
        
        #the below results in {0: '2c', 1: '3c', 2: '4c', 3: '5c', 4: '6c', 5: '7c',...}
        self._deck_map = dict(enumerate(self.all_cards))
        
        #the below results in an inverted deck map sorted by card ranks:
        #{'9h': 33, '10h': 34, '7d': 18, '7c': 5, '10c': 8,...}
        self._deck_map_reverse_list = [(i+j,v) for v,(i,j) in enumerate(zip(self.ranks*4,sorted(self.suits*13)))]
        self._deck_map_reverse_dict = dict(self._deck_map_reverse_list)
        
        #the below results in map of ranks only:
        #{'A': 12, '10': 8, 'K': 11, 'J': 9, 'Q': 10, ...}
        self.rankstonum = [(j,i) for i,j in enumerate(self.ranks)]
        self.rankstonum_dict = dict(self.rankstonum)
        
        self._deck=[]

    
    def reset(self,seq=None):
        
        warnings.warn("deprecated")


    def retrieve(self,nbcards):
        '''
        return a list of card numbers from the sorted deck
        and removes those card numbers from the deck
        '''
        #TODO: need check that enough cards in deck
        return [self._deck.pop() for c in range(nbcards)]
        
    


    def get_sequences(self,seqs=[[]]):
        '''
        returns sequences of card numbers associated to the card values
        in seqs.  If a card value only specify a rank then retrieve
        a corresponding card number from same rank from a randomly sorted
        deck.
        Removes the selected cards numbers from the deck before returning
        the result.
        The deck is saved as a field of Deck for use in the draw steps. 
        '''
        
        drev=self._deck_map_reverse_list
        drevd=self._deck_map_reverse_dict
        
        fullcards=self._getfullcards(drevd, seqs)
        rankcards=self._getrankcards(seqs)
                
        fullcardsmerge=[i for o in fullcards for i in o]
        
        randdeck=random.sample(range(52),52)
        tree=self._gettree(randdeck,fullcardsmerge)

        anysuitcardsseqs=self._getanysuitcardsseqs(tree,rankcards)

        fin_seqs=self._getfinseqs(fullcards,anysuitcardsseqs)
        
        tp_list=[j for seq in fin_seqs for j in seq]
        
        self._deck=self._getremainingdeck(tp_list,randdeck)
        
        return fin_seqs
        
    
    def _getremainingdeck(self,tp_list,randdeck):
        '''return the cards in deck excluding the cards
        in tp_list 
        '''
        return filter(lambda x: x not in tp_list,randdeck)    


    def _gettree(self,randdeck,fullcardsmerge):
        '''create a tree of card numbers grouped by rank and randomly sorted within each group
        and map those group to their respective ranks
        '''
        tp_range=range(13)
        return [(v,(lambda v: (i for i in randdeck if i % 13 == v and i not in fullcardsmerge))(v)) for v in tp_range]

    
    def _getfinseqs(self,fullcards,anysuitcardsseqs):
        '''merges the two partial sequences while keeping
        the original list structure
        '''
        tp_fc_len=fullcards.__len__()
        return [anysuitcardsseqs[i]+fullcards[i] for i in range(tp_fc_len)]
    
    
    def _getanysuitcardsseqs(self,tree,rankcards):
        '''retrieve a card number from tree having same rank
        as the cards in rankcards
        '''
        return [[j.next() for v,j in tree for i in seq if i==v] for seq in rankcards]
        
        
    def _getrankcards(self,seqs):
        '''retrieve rank numbers associated to the card values in seqs
        that only have a rank specified such as 'K' or 'J' or '7'
        '''
        return [[self.rankstonum_dict[i] for i in seq if i in self.ranks] for seq in seqs]
    
    
    def _getfullcards(self,drevd,seqs):
        '''retrieve card numbers associated to the card values in seqs
        that have a rank and suit specified, such as '10d' or 'Ac'
        '''
        return [[self._deck_map_reverse_dict[v] for v in seq if v not in self.ranks] for seq in seqs]
        
    
    
        