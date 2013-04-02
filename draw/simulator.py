'''
Created on Mar 28, 2013

@author: jule64@gmail.com
'''

from draw import deck, strategy, player
import SystemEvents
import sys
import cProfile

class Simulator():
    '''
    
    '''


    def __init__(self):
        '''
        
        '''
        pass
    
    
def run_simu(strat,seq,nbdraws,_runs,carddeck):
    
    h1tp=seq
    
    
    
    
    
#    h2tp=[]
#    h3tp=[]
    
    s1=strategy.Strategy(strat)
#    s2=strategy.Strategy(5)
#    s3=strategy.Strategy(5)
    
    
    count1=0
#    count2=0
#    count3=0
    
    run=_runs
    for i in range(run):
        


        s1.reset()
#        s2.reset()
#        s3.reset()
        
        #generate a fresh new sequence of cards from
        #the initial stubs
#        seqs=carddeck.get_sequences([h1tp,h2tp,h3tp])
        seqs=carddeck.get_sequences([h1tp])
        
#        print str([seqs[0][i]%13 for i in range(5)])
        
        
        h1=seqs[0]
#        h2=seqs[1]
#        h3=seqs[2]
                        
        #initialise deck
#        carddeck.reset(h1+h2+h3)
        carddeck.reset(h1)
        
        p1=player.Player(carddeck, s1, h1)
#        p2=player.Player(carddeck, s2, h2)
#        p3=player.Player(carddeck, s3, h3)
        
#        print "starting player seq is "+str(p1._seq)
        
        #simulate initial cards dealt
        p1.draw()
#        p2.draw()
#        p3.draw()
        
#        print "player seq after initial dealing is "+str(p1._seq)
        
        
        #simulate three draws plus
        #card selection
        for v in range(nbdraws):
            p1.select_cards()
#            p2.select_cards()
#            p3.select_cards()
            
            p1.draw()
#            p2.draw()
#            p3.draw()
        
        
        p1.check_last()
#        p2.check_last()
#        p3.check_last()
        
        #printout the final hand
        
        #if p1.issuccess and (p1._seq[3]%13)!=6:
        
        #the below line keeps only J lows
        if p1.issuccess and max([p1._seq[i]%13 for i in range(5)])==strat:
        #if p1.issuccess:
            count1=count1+1
#            print [p1._seq[i]%13+2 for i in range(5)]
            
            
#            print str([p1._seq[i]%13+2 for i in range(5)])

#        if p2.issuccess:
#            count2=count2+1
#
#        if p3.issuccess:
#            count3=count3+1

    
#    totalcount=count1+count2+count3
#        if i%10000==0 and i>0:
#            print str(i) +"  "+ str((count1+0.0)/i)
        
    return (count1+0.0)/run
#    print "p2 is " +str((count2+0.0)/run)
#    print "p3 is " +str((count3+0.0)/run)
        

def startme():   
    carddeck = deck.Deck()
    
    runs=50000
    
    #nber of draws
    for u in [0]:
        print "Nber of draws left: "+str(u)
        print ""
            
        #strategy
        for j in [9]:
            print "Target: "+str(j+2)+" low"
            print ""
            print "starting hand\t|  Odds (%)"
            
            #hands
            #[],['2'],['2','3','4','5'],['2','3','4','7']
            for i in [[]]:
                
                g=0
                if i.__len__()>4:
                    g=1
                s=""
                for d in i:
                    s=s+str(d)+","
                
                if i==[]:
                    s="any 5 cards"
                    g=1
                
                
                print s[:-1] + ['\t\t','\t'][g]+"|  " + str(run_simu(j,i,u,runs,carddeck)*100)
            
            print ""
            print ""   
    
    

if __name__ == "__main__":
    
    '''
    Run a 7 low strategy 1000 times
    in which one player has all the cards
    except a 7.
    
    '''
    
    startme()
#    cProfile.run('startme()')

    
    
    