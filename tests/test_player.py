'''
Created on Mar 27, 2013

@author: jule64@gmail.com
'''
import unittest
from draw import deck, strategy, player


class TestPlayer(unittest.TestCase):
    '''
    classdocs
    '''

       
       
    def test_starting_sequence_is_null(self):
        
        carddeck = deck.Deck()
        s1 = strategy.Strategy(6)
        p1 = player.Player(carddeck, s1)
        self.assertEqual(p1._seq.__len__(), 0)
    
       
    def test_starting_sequence_values(self):
        
        dk = deck.Deck()
        s1 = strategy.Strategy(6)
        seq=dk.get_sequences([['2c','5c','10c','6s']])[0]
        p1 = player.Player(dk, s1,seq)
        self.assertEqual(p1._seq, [0,3,8,43])


    def test_cards_after_draw(self):
        '''
        Test that 5 cards are left in the player's hands
        after a draw
        '''
        carddeck = deck.Deck()
        carddeck.reset()
        s1 = strategy.Strategy(6)
        p1 = player.Player(carddeck, s1)
        p1.draw()
        self.assertEqual(p1._seq.__len__(), 5)
    
    
    def test_cards_after_selection(self):
        '''
        Test that the number of cards in the
        player's hands after running the card
        selection strategy is between 0 and 5
        '''        
        carddeck = deck.Deck()
        carddeck.reset()
        s1 = strategy.Strategy(6)
        p1 = player.Player(carddeck, s1)
        p1.draw()
        p1.select_cards()
        self.assertEqual(0<=p1._seq.__len__()<6, True)
    
    
    def test_check_last_draw(self):
        '''
        Test that the issuccess field of
        Player is set to True if the strategy
        was successful and False otherwise
        '''
        carddeck = deck.Deck()
        
        carddeck.reset()
        
        finalseq=carddeck.get_sequences([['2c','3c','4d','6s','8h']])[0]
        s1 = strategy.Strategy(6)
        
        
        p1 = player.Player(carddeck, s1,finalseq)
        p1.check_last()
        
        self.assertEqual(p1.issuccess, True)
        
        
        finalseq=carddeck.get_sequences([['2c','3c','4d','6s','Jh']])[0]
        s1 = strategy.Strategy(6)
        
        p1 = player.Player(carddeck, s1,finalseq)
        p1.check_last()
        
        self.assertEqual(p1.issuccess, False)
        
        #check that check_last() does not incur cards to be
        #removed from seq when strategy was not successful.
        #Here we test that Jh is still in the final seq 
        self.assertEqual(p1._seq[4], 35)
        
        
    
    
    
