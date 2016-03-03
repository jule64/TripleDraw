import sys


class CardRules(object):

    def __init__(self):
        self.is_final_check = False
        self.issuccess=True

    def set_target(self,target):
        self.target=target

    def apply_rules(self, integer_hand):
        
        '''
        passes the int sequence into a series of decision rules
        to determine what cards in the sequence to keep and
        returns a sequence of cards to keep
        '''
        #here are the ranks
        #0: '2c', 1: '3c', 2: '4c', 3: '5c', 4: '6c', 5: '7c', 6: '8c',
        #7: '9c', 8: '10c', 9: 'Jc', 10: 'Qc', 11: 'Kc', 12: 'Ac'

        teststraight=True
        testflush=True

        straightindex=1
        flushindex=1

        #order seq on card rank, i.e. 2,3,..,K,A
        tp_seq=[(c%13,c) for c in integer_hand]
        tp_seq.sort()
        integer_hand=[c for i, c in tp_seq]

        #find the suit number of the suit most found in seq
        #store suit of each cards in seq
        seq_suits=[c / 13 for c in integer_hand]
        #find the suit number of the most found suit
        dominant_suit=max([(seq_suits.count(i),i) for i in range(4)])[1]

        for curindex,card in enumerate(integer_hand):

            #checking if card rank is equal to or less than target rank
            if card%13 > self.target:
                if(self.is_final_check):
                    # we have a high card in the hand hence no need to carry on
                    return False
                #mark card rejected
                integer_hand[curindex]=None
                continue

            elif curindex>0:
            
                #checking for pairs
                prev_card = integer_hand[curindex-1]
                if prev_card!=None and card%13==prev_card%13:
                    if(self.is_final_check):
                        # we have a pair in the hand hence no need to carry on
                        return False

                    #check if card belongs to the dominant suit
                    if card/13==dominant_suit:
                        #swap card with prev_card and mark card rejected
                        integer_hand[curindex - 1]=None
                        integer_hand[curindex]=prev_card
                    else:
                        #mark prev_card rejected
                        integer_hand[curindex - 1]=None
                    #since there is a pair we don't need to test for straigth and flush
                    teststraight=False
                    testflush=False
                    continue
                else:
                    if teststraight:
                        # check if card and prev_card follow each other
                        if abs(card%13-prev_card%13)==1:
                            # we increment an index, later we check if the index = 5, meaning there is a straight
                            straightindex+=1

                            if straightindex==5:
                                if(self.is_final_check):
                                    # we have a straight in the hand hence no need to carry on
                                    return False
                                #remove top card if lowest card is a 2, else remove the 2nd top card
                                if integer_hand[0]%13==0:
                                    integer_hand[4]=None
                                else:
                                    integer_hand[3]=None
                                flushindex=0
                                continue

                        else:
                            # no risk of a straight hence no need to test anymore
                            teststraight = False

                    if testflush:
                        # we test if card and prev_card have same suit (color)
                        if card/12==prev_card/12:
                            flushindex+=1

                            if flushindex==5:
                                if(self.is_final_check):
                                    # we have a flush in the hand hence no need to carry on
                                    return False
                                #reject second highest card
                                #NOTE: in reality there are special cases where it is preferable to throw an other
                                #card, such as in the case of a 8,7,5,3,2 drawing to a 9 low.
                                #TODO: create a static table of special cases of draw after a flush
                                integer_hand[-2]=None
                                continue
                        else:
                            testflush = False

        if not self.is_final_check:
            # return only the cards that have been retained
            return [c for c in integer_hand if c != None]
        else:
            # The hand was successful
            return True


    def set_final_check(self):
        self.is_final_check = True

        
        
        