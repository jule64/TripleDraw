'''
Created on Mar 26, 2013

@author: jule64@gmail.com
'''

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, deck,strategy,startseq=[]):
        '''
        Constructor
        '''
        self._deck = deck
        self._MAXCARDS = 5
        self._strategy = strategy
        
        self._startseq=startseq
        self._seq=startseq
        self.issuccess=False
        
    
    
    #not used currently
    def reset(self,seq):
        '''
        Rest a player with the starting sequence
        '''
        
        self._seq=self._startseq
        
        
    
    
    def draw(self):
        
        self._seq=self._seq+self._deck.retrieve(self._MAXCARDS-self._seq.__len__())
    
    
    def select_cards(self):
        '''
        Returns the sequence of cards to keep as per the chosen
        strategy.
        This should be run after every draw except
        the last draw
        '''
        self._seq = self._strategy.run(self._seq)
        

    def check_last(self):
        '''
        Call the strategy on the final hand to
        determine if the strategy succeeded
        '''
             
        self.issuccess=self._strategy.run(list(self._seq),True)
        
        
        