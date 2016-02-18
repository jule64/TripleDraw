'''
Created on Mar 28, 2013

@author: jule64@gmail.com
'''

from draw import strategy, player
from draw.deck import Deck
import cProfile

class Simulator():
    '''
    Main Class where the user can create
    scenarios and run simulations
    
    NOTE: need to create interface for implementing simulations
    instead of freeform like here..
    
    '''



    
    def run_simu(self,strat,raw_seqs,nbdraws,_runs,carddeck):

        
        s1=strategy.Strategy(strat)
        
        
        count1=0
        
        run=_runs
        for i in range(run):
    
            s1.reset()
            
            #generate a fresh new sequence of cards from
            #the initial stubs
            #this also creates a shuffled deck wich excludes
            #any cards provided in raw_seqs
            seqs=carddeck.get_sequences(raw_seqs)
            
            h1=seqs[0]
                            

            
            p1=player.Player(carddeck, s1, h1)
            
            #simulate initial cards dealt
            p1.draw()
            
            #simulate three draws plus
            #card selection
            #this code is skipped if nber of
            #draws is set to 0 in startme()
            for v in range(nbdraws):
                p1.select_cards()
                
                p1.draw()
            
            p1.check_last()
            
            #the below line keeps only Jack lows
            #if p1.issuccess and max([p1._seq[i]%13 for i in range(5)])==strat:
            
            if p1.issuccess:
                count1=count1+1
                
        return (count1+0.0)/run
        
    @staticmethod
    def startme():   
        
        simulator = Simulator()
        
        carddeck = Deck()
        
        runs=15000
        
        #nber of draws
        for u in [0]:
            print "Nber of draws left: "+str(u)
            print ""
                
            #strategy - 9 means J low
            for j in [9,8]:
                print "Target: "+str(j+2)+" low"
                print ""
                print "starting hand\t|  Odds (%)"
                
                #hands
                #the first list is the hand representing the player's
                #cards that we want to see in the starting hand.  Can be
                #left blanc.
                #the second list holds the dead cards, which is the cards that
                #we assume are not in the deck.  This is useful to simulate when
                #a card is in the opponent's hands.
                #example of pre draw list:
                #[['2',''9'],['2','3','5']]
                for i in [[[],[]]]:
                    
                    g=0
                    if i.__len__()>4:
                        g=1
                    s=""
                    for d in i:
                        s=s+str(d)+","
                    
                    if i==[]:
                        s="any 5 cards"
                        g=1
                    
                    
                    print s[:-1] + ['\t\t','\t'][g]+"|  " + str(simulator.run_simu(j,i,u,runs,carddeck)*100)
                
                print ""
                print ""   
        
        

if __name__ == "__main__":
    
    Simulator.startme()
    
    #the line below is used for profiling
#     cProfile.run('Simulator.startme()')

    
    
    