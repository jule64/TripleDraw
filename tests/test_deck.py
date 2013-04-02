'''
Created on Mar 27, 2013

@author: jule64@gmail.com
'''


import unittest
from draw import deck

class TestDeck(unittest.TestCase):
    '''
    classdocs
    '''



    def test_initialise(self):
        '''
        Deck should be created and shuffled with all
        52 cards
        '''
        
        d=deck.Deck()
        d.reset()
        
        self.assertEqual(d._deck.__len__(),52)


    
    
    def test_initialise_with_existing_sequence(self):
        '''
        Deck should be created and shuffled without the card sequence
        provided as parameter
        '''
        
        card_seq=['2d','Jc','Kc','Qs']
        
        d=deck.Deck()
        seqs=d.get_sequences([card_seq])
        d.reset(seqs[0])
        
        self.assertEqual(d._deck.__len__(),52-card_seq.__len__())


    
    def test_retrieve_cards(self):
        '''
        Initialise a new deck and retrieve a set number of
        cards from it.
        '''
        d=deck.Deck()
        d.reset()
        
        self.assertEqual(d.retrieve(3).__len__(),3)

        

    def test_generate_sequence(self):
        #we want a sequences that hodls hands that hold any suit of a
        #rank or full cards
        testseqs=[['10h', '3', 'Kc'], ['2', '3', 'Qd'], []]
        
        d = deck.Deck()
        
        final_seqs = d.get_sequences(testseqs)
        
        #checking than length of final seqs is same as orginal
        #and has same number of cards as original seqs
        #Note: this is a very weak check. a more thorough one
        #would involve chekcing that the suit or the half formed
        #cards in original sequence are same as that of the fully
        #formed ones
        self.assertEqual(final_seqs.__len__(), 3)



if __name__ == "__main__":
    
    unittest.main(verbosity=2)
        
        
        