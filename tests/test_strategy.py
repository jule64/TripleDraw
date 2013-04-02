'''
Created on Mar 27, 2013

@author: jule64@gmail.com


Sorted Deck Mapping:
#0: '2c', 13: '2d', 26: '2h', 39: '2s', 1: '3c', 14: '3d'
#, 27: '3h', 40: '3s', 2: '4c', 15: '4d', 28: '4h', 41: '4s'
#, 3: '5c', 16: '5d', 29: '5h', 42: '5s', 4: '6c', 17: '6d'
#, 30: '6h', 43: '6s', 5: '7c', 18: '7d', 31: '7h', 44: '7s'
#, 6: '8c', 19: '8d', 32: '8h', 45: '8s', 7: '9c', 20: '9d'
#, 33: '9h', 46: '9s', 8: '10c', 21: '10d', 34: '10h', 47: '10s'
#, 9: 'Jc', 22: 'Jd', 35: 'Jh', 48: 'Js', 10: 'Qc', 23: 'Qd'
#, 36: 'Qh', 49: 'Qs', 11: 'Kc', 24: 'Kd', 37: 'Kh', 50: 'Ks'
#, 12: 'Ac', 25: 'Ad', 38: 'Ah', 51: 'As'


'''

import unittest
from draw import strategy

class SimuTests(unittest.TestCase):
    '''
    classdocs
    '''
    
    
    def test_strategy_no_overcards_7_low(self):
        '''
        testing a strategy of throwing all cards
        greater than the target (e.g. 7 low)
        
        under this test, only the cards ranking less than 7
        should be kept by the strategy
        
        '''
        s = strategy.Strategy(5)
        
        #starting hand is 2c,4h,6s,Ks,Jc
        start_seq = [0,28,43,50,9] 
        
        #expected returned sequence is 2c,4h,6s
        exp_seq = [0,28,43]
        
        #testing that the sequence returned by the strategy matches the
        #expected sequence        
        self.assertEqual(s.run(start_seq),exp_seq)
    
 
    def test_strategy_no_overcards_9_low(self):
        '''
        Same as previous but with a 9 low target
        '''
        s = strategy.Strategy(7)
        start_seq = [0,28,46,50,9] 
        exp_seq = [0,28,46]
        self.assertEqual(s.run(start_seq),exp_seq) 
 
 
    def test_break_pairs(self):
        '''
        Break pair
        If one of the pair suit belongs to most numbered suit
        in the sequence, that card should be thrown in order
        to avoid Flush risk on next draw.
        This is tested under a 8 low strategy
        '''
        s = strategy.Strategy(6)
        
        #hand: 2c,3c,4c,4d,5s
        start_seq = [0,1,2,15,42] 
        exp_seq = [0,1,15,42]
        self.assertEqual(s.run(start_seq),exp_seq) 
 
        
        
 
    def test_strategy_break_straight_normal(self):
        '''
        Testing a strategy of throwing away the second top
        ranked card if the starting sequence is a straight

        This test is conducted under a 9low drawing strategy
        '''
        s = strategy.Strategy(7)
        
        #starting hand is 5c,6h,7s,8s,9d
        start_seq = [3,30,44,45,20]
        
        #expected returned sequence is 5c,6h,7s,9d
        exp_seq = [3,30,44,20]
        
        #testing that the sequence returned by the strategy matches the
        #expected sequence  
        self.assertEqual(s.run(start_seq),exp_seq)      
    
    
    def test_strategy_break_straight_if_two(self):
        '''
        Testing a strategy of throwing away the highest card
        in the sequence if the sequence is a straight starting
        with 2

        This test is conducted under a 8low drawing strategy
        
        '''
        s = strategy.Strategy(6)
        
        #starting hand is 2c,3h,4s,5s,6d
        start_seq = [0,27,41,42,17]
        
        #expected returned sequence is 2c,3h,4s,5s
        exp_seq = [0,27,41,42]
        
        #testing that the sequence returned by the strategy matches the
        #expected sequence  
        self.assertEqual(s.run(start_seq),exp_seq)    

   

    def test_strategy_break_flush_8_low(self):
        '''
        Testing a strategy of throwing away the second top
        ranked card if the starting sequence is a Flush

        This test is conducted under a 8low drawing strategy
        
        '''
        s = strategy.Strategy(6)
        
        #starting hand is 2c,3c,4c,5c,8c
        start_seq = [0,1,2,3,6]
        
        #expected returned sequence is 2c,3h,4s,5s
        exp_seq = [0,1,2,6]
        
        #testing that the sequence returned by the strategy matches the
        #expected sequence  
        self.assertEqual(s.run(start_seq),exp_seq)  



if __name__ == "__main__":
    
    unittest.main(verbosity=2)