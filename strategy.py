import sys


class Strategy(object):

    def __init__(self, target=9):
        '''
        params should say wether the aim is to draw 7 low
        or 9 low etc
        '''
        self.target=target
        self.issuccess=True
        
        
    def reset(self):
        self.issuccess=True
        

    def run(self,seq,finalcheck=False):
        
        '''
        passes the sequence into a series of decision rules
        to determine what cards in the sequence to keep and
        returns a sequence of cards to keep
        '''
        #here are the ranks
        #0: '2c', 1: '3c', 2: '4c', 3: '5c', 4: '6c', 5: '7c', 6: '8c',
        #7: '9c', 8: '10c', 9: 'Jc', 10: 'Qc', 11: 'Kc', 12: 'Ac'
        
        
        teststraight=True
        testflush=True
        
        straightindex=0
        flushindex=0
        
        
        #order seq on card rank, i.e. 2,3,..,K,A
        tp_seq=[(c%13,c) for c in seq]
        tp_seq.sort()
        seq=[c for i,c in tp_seq]
        
        
        #find the suit number of the suit most found in seq
        #store suit of each cards in seq
        seq_suits=[c/13 for c in seq]
        #find the suit number of the most found suit
        domsuit=max([(seq_suits.count(i),i) for i in range(4)])[1]
        
        for i in seq:
            curindex=seq.index(i)
            
            #checking if card of any suit is equal to or less than target rank
            if i%13 > self.target:
                #reject card
                seq[curindex]=None
                self.set_is_failed(finalcheck)
                
                
            elif curindex>0:
            
                #checking for pairs (or higher)
                if seq[curindex-1]!=None and i%13==seq[curindex-1]%13:
                    #check if i belongs to the dominante suit
                    if i/13==domsuit:
                        #reject i
                        tpval=seq[curindex-1]
                        
                        seq[curindex-1]=None
                        seq[curindex]=tpval
                        
                        
                    else:
                        #reject j
                        seq[curindex-1]=None
                    #straigth does not need to be tested
                    teststraight=False
                    testflush=False
                    self.set_is_failed(finalcheck)            
                
                else:
                    if teststraight:
                        if abs(i%13-seq[curindex-1]%13)==1:
                            straightindex=straightindex+1
                    if testflush:
                        if i/12==seq[curindex-1]/12:
                            flushindex=flushindex+1
            
        if straightindex==4:
            #remove top card if lowest card
            #is a 2, else remove the 2nd top
            #card
            if seq[0]%13==0:
                seq[4]=None
            else:
                seq[3]=None
            flushindex=0
            self.set_is_failed(finalcheck)
            
        if flushindex==4:
            #remove second highest card
            #NOTE: in reality there are special cases
            #where it is preferable to throw other cards
            #card, such as in the case of a 8,7,5,3,2
            #drawing to a 9 low.
            #TODO: create a static table of special cases
            #of draw after a flush
            seq[3]=None
            self.set_is_failed(finalcheck)
    
        if finalcheck == False:
            return [c for c in seq if c != None]          
        
        return self.issuccess
        
        

    def set_is_failed(self,finalcheck):
        
        
        if finalcheck==False:
            return
        
        self.issuccess=False
        
        
        
        
        
        