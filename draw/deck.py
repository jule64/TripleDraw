'''
Created on Mar 26, 2013

@author: jule64@gmail.com



Sorted Deck Mapping:
#0: '2c', 1: '3c', 2: '4c', 3: '5c', 4: '6c', 5: '7c', 6: '8c', 7: '9c', 8: '10c'
#, 9: 'Jc', 10: 'Qc', 11: 'Kc', 12: 'Ac', 13: '2d', 14: '3d', 15: '4d', 16: '5d'
#, 17: '6d', 18: '7d', 19: '8d', 20: '9d', 21: '10d', 22: 'Jd', 23: 'Qd', 24: 'Kd'
#, 25: 'Ad', 26: '2h', 27: '3h', 28: '4h', 29: '5h', 30: '6h', 31: '7h', 32: '8h'
#, 33: '9h', 34: '10h', 35: 'Jh', 36: 'Qh', 37: 'Kh', 38: 'Ah', 39: '2s', 40: '3s'
#, 41: '4s', 42: '5s', 43: '6s', 44: '7s', 45: '8s', 46: '9s', 47: '10s', 48: 'Js'
#, 49: 'Qs', 50: 'Ks', 51: 'As'

'''


import random
import itertools

class Deck(object):
    '''
    the deck can be initialised with specific cards
    removed from it so as to simulate specific
    starting hands situation.
    For example, if we want to simulate a starting
    hand of 2c,4c,6d we can pass that hand in the
    reset method parameter and a new deck will be
    initialised without those cards in it.
    
    '''


    def __init__(self):
        '''
        Initialises map structures
        '''
        
        suits = ["s","c","d","h"]
        self.ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.all_cards=[i+j for i,j in zip(self.ranks*4,sorted(suits*13))]
        
        #the below results in {0: '2c', 1: '3c', 2: '4c', 3: '5c', 4: '6c', 5: '7c',...}
        self._deck_map = dict(enumerate(self.all_cards))
        
        #the below results in {'9h': 33, '10h': 34, '7d': 18, '7c': 5, '10c': 8,...}
        self._deck_map_reverse_list = [(i+j,v) for v,(i,j) in enumerate(zip(self.ranks*4,sorted(suits*13)))]
        self._deck_map_reverse_dict = dict(self._deck_map_reverse_list)
        
        #the below results in {'A': 12, '10': 8, 'K': 11, 'J': 9, 'Q': 10, ...}
        self.rankstonum = [(j,i) for i,j in enumerate(self.ranks)]
        self.rankstonum_dict = dict(self.rankstonum)
        
        
        self._deck=[]
#        self.reset()



    def reset(self,seq=None):
        '''
        Creates a new, shuffled deck
        seq is a sequence of cards. If
        seq is provided, the deck will 
        be initialise without these cards
        '''
        pass
        if seq!=None:
            
            #convert literal cards sequence into
            #a sequence of numbers
            self._deck = list(set(range(52))-set(seq))
        else:
            self._deck = range(52)
        
        random.shuffle(self._deck)
        
    def retrieve(self,nbcards):
        '''
        return a list of card numbers and removes those card
        numbers from the deck
        '''
        
        # need check that enough cards in deck
        return [self._deck.pop() for c in range(nbcards)]
        
    


    def get_sequences(self,seqs):
        
        '''
        create a tree of randomly sorted cards grouped by rank and
        pop cards from the desired rank
        returns a list of one or more sequences
        '''
        
        #step 1: identify full cards (cards with a rank and suit) in seqs and
        #remove them from the deck
        
        drev=self._deck_map_reverse_list
        drevd=self._deck_map_reverse_dict
        
        #create list of lists that contains the card number of the full cards
        #found in seqs.
        #this construction in chosen in order to keep the original order in which
        #the cards were submitted in seqs 

#prof        fullcards=[[drevd[i] for i in seq if i in [z for z,q in drev]] for seq in seqs]
        fullcards=self._getfullcards(drevd, seqs)
        rankcards=self._getrankcards(seqs)
        
#        print rankcards 
        
        #remove the full cards from the deck
#        fullcardsmerge=list(itertools.chain(*fullcards))
        
        fullcardsmerge=[i for o in fullcards for i in o]
        
#prof        tpdeck = list(set(range(52))-set(fullcardsmerge))
        
        #create a tree cards grouped by rank that are randomly sorted within each group
        #and which excludes any card that was removed from the deck in the previous step
        #this looks like {'A': [12, 38, 25, 51], '10': [34, 47, 21, 8], 'K': [24, 11, 37, 50],...}
        
        #shuffle deck for prep of tree 
#prof        random.shuffle(tpdeck)
        
        randdeck=random.sample(range(52),52)

#        randdeck=range(52)
#        random.shuffle(randdeck)


        
#        randdeck=range(52)
        #!!! this is potentialy compute intensive
#prof        tpdeck=[i for i in randdeck if i not in fullcardsmerge]

        
        #tree=dict([(j,[i for i in tpdeck if i%13==v]) for j,v in self.rankstonum])
        #tree=dict([(v,(i for i in randdeck if i%13==v and i not in fullcardsmerge)) for j,v in self.rankstonum])
        
#        tree=[(v,(i for i in randdeck if i%13==v and i not in fullcardsmerge)) for j,v in self.rankstonum]
        
        tree=self._gettree(randdeck,fullcardsmerge)

        
        
        #copy from seqs the cards that don't have a suit
#        rankseqs=[[j for j in i if j in [v for v,h in self.rankstonum]] for i in seqs]
        
        #for each rank in rankseqs extract a card from tree having same rank
        #by extracting the card we ensure the card is removed from tree for the
        #next iteration of value in rankseqs 
        anysuitcardsseqs=self._getanysuitcardsseqs(tree,rankcards)
#        print anysuitcardsseqs
        
        #merge full cards and any suit cards as per seqs
        #note: the original order in which the cards were submitted is not
        #preserved but the oder of the sequences is
        fin_seqs=self._getfinseqs(fullcards,anysuitcardsseqs)
        
#        fin_seqs=[i[0] for i in [[i+j for v,i in enumerate(fullcards) if v==q] for q,j in enumerate(anysuitcardsseqs)]]
#        print fin_seqs
        tp_list=[j for seq in fin_seqs for j in seq]
#        self._deck=[i for i in randdeck if i not in tp_list]
        
        self._deck=self._getremainingdeck(tp_list,randdeck)
        
        #[i for i in randdeck if i not in [j for seq in fin_seqs for j in seq]]
        
        #return the result to the caller
#        print 'print seqs'
#        print randdeck
#        print fin_seqs
#        print self._deck
        return fin_seqs
        
    
    def _getremainingdeck(self,tp_list,randdeck):
        return filter(lambda x: x not in tp_list,randdeck)    


    def _gettree(self,randdeck,fullcardsmerge):
        #[(v,(i for i in randdeck if i%13==v and i not in fullcardsmerge)) for j,v in self.rankstonum]
        tp_range=range(13)
        return [(v,(lambda v: (i for i in randdeck if i % 13 == v and i not in fullcardsmerge))(v)) for v in tp_range]
    
    def _getfinseqs(self,fullcards,anysuitcardsseqs):
        tp_fc_len=fullcards.__len__()
        return [anysuitcardsseqs[i]+fullcards[i] for i in range(tp_fc_len)]
    
    
    
    def _getanysuitcardsseqs(self,tree,rankcards):
        
        return [[j.next() for v,j in tree for i in seq if i==v] for seq in rankcards]
        
        
        
    def _getrankcards(self,seqs):
        
        return [[self.rankstonum_dict[i] for i in seq if i in self.ranks] for seq in seqs]
    
    
    
    def _getfullcards(self,drevd,seqs):
        
        return [[self._deck_map_reverse_dict[v] for v in seq if v not in self.ranks] for seq in seqs]
        
    
    
        