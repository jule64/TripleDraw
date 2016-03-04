import sys

import cardutils


class CardRules(object):

    def __init__(self, deck):
        self.deck = deck
        self.check_success = False
        self.issuccess=True

    def set_target(self,target_rank):
        self.integer_target_rank=self.deck.convert_rank_to_int(target_rank)

    def apply_rules(self, hand):
        
        '''
        Runs the cards in the hand through a series of decision rules
        to determine which cards to keep and then return a list of only
        those cards that were retained.

        @:returns retained_cards or True/False on last check
        '''

        teststraight=True
        testflush=True

        straightindex=0
        flushindex=0

        # Converting the hand to integers in order to apply the
        # decision rules.  This follow the integer to card mapping defined
        # in deck, such that '2c' is integer 0, '3c' is integer 1, etc.
        integer_hand = cardutils.convert_cards_to_integers(hand,self.deck)

        # order cards in integer_hand by rank regardless of suit,
        # e.g. [2c,2s,8d,Js,Jh]
        temp_list=[(c%13,c) for c in integer_hand]
        temp_list.sort()
        rank_ordered_integer_hand=[c for i, c in temp_list]


        #first remove any card which rank is greater than the target rank
        for card_index,card in enumerate(rank_ordered_integer_hand):

            if card%13 > self.integer_target_rank:
                if(self.check_success):
                    # we have a high card in the hand hence no need to carry on
                    return False
                #mark card rejected
                rank_ordered_integer_hand[card_index]=None

                #since there are less than 5 valid cards we don't need to test for straight and flush
                teststraight=False
                testflush=False
                continue

        if(None in rank_ordered_integer_hand):
            # rebuild the list with only cards that we are keeping
            rank_ordered_integer_hand = [c for c in rank_ordered_integer_hand if c is not None]

        #we make sure we have at least two cards to run the next rules
        if(len(rank_ordered_integer_hand)>1):
            #of the cards left we check for paired cards, straights and flushes
            for card_index,card in enumerate(rank_ordered_integer_hand):

                if(card_index==0):
                    continue

                #checking for pairs
                prev_card = rank_ordered_integer_hand[card_index-1]
                if card%13==prev_card%13:
                    if(self.check_success):
                        # we have a pair in the hand hence no need to carry on
                        return False

                    # find the suit number of the suit most present in the hand (called
                    # dominant suit), it will be used when deciding which card to remove in a pair
                    cards_suits=[c / 13 for c in rank_ordered_integer_hand if c is not None]
                    dominant_suit=max([(cards_suits.count(i),i) for i in range(4)])[1]

                    #check if card belongs to the dominant suit
                    if card/13==dominant_suit:
                        #swap card with prev_card and mark card rejected
                        rank_ordered_integer_hand[card_index - 1]=None
                        rank_ordered_integer_hand[card_index]=prev_card
                    else:
                        #mark prev_card rejected
                        rank_ordered_integer_hand[card_index - 1]=None
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

                            #if straightindex = 4 this means that the five cards in the hand form a straight
                            if straightindex==4:
                                if(self.check_success):
                                    # we have a straight in the hand hence not success
                                    return False
                                #remove top card if lowest card is a 2, else remove the 2nd top card
                                if rank_ordered_integer_hand[0]%13==0:
                                    rank_ordered_integer_hand[4]=None
                                else:
                                    rank_ordered_integer_hand[3]=None
                                flushindex=0
                                continue

                        else:
                            # no risk of a straight hence no need to test anymore
                            teststraight = False

                    if testflush:
                        # we test if card and prev_card have same suit (color)
                        if card/12==prev_card/12:
                            flushindex+=1

                            # if flushindex = 4 this means that the five cards in the hand form a flush
                            if flushindex==4:
                                if(self.check_success):
                                    # we have a flush in the hand hence no need to carry on
                                    return False
                                #reject second highest card
                                #NOTE: in reality there are special cases where it is preferable to throw an other
                                #card, such as in the case of a 8,7,5,3,2 drawing to a 9 low.
                                #TODO: create a static table of special cases of draw after a flush
                                rank_ordered_integer_hand[-2]=None
                                continue
                        else:
                            testflush = False
            # <- end of for loop ->

        if not self.check_success:
            # return only the cards that have been retained
            if(None in rank_ordered_integer_hand):
                rank_ordered_integer_hand = [c for c in rank_ordered_integer_hand if c is not None]
            return cardutils.convert_integer_cards_to_cards(rank_ordered_integer_hand,self.deck)
        else:
            # The hand was successful
            return True


    def set_final_check(self):
        self.check_success = True

    def is_success(self, cards_in_hand):
        '''
        Checks whether the hand is a valid triple draw hand or not.
        Unlike calling `apply_rules(cards_in_hand)` directly, calling this method
        will NOT modify the list passed to it.

        :param cards_in_hand:
        :return: True if the hand is a valid triple draw hand, False if not
        '''
        self.check_success = True
        return self.apply_rules(cards_in_hand)
