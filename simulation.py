from colors import red

from cardrules import CardRules
from deck import Deck


class Simulation(object):
    '''
    The main simulation object
    '''

    def __init__(self,starting_cards=None, number_draws=None, target=None, simulations=None, plot=None):

        self.starting_cards=starting_cards
        self.number_of_draws=number_draws
        self.target_rank=target
        self.number_simulations=simulations
        self.is_plot = plot
        self.MAX_CARDS_IN_HAND=5
        self._intermediate_results = []
        self._simulation_result = None

    def launch(self):
        '''
        Runs a simulation
        :return: double: the ratio of successful hands over total hands
        '''
        success_count = 0
        deck = Deck()

        for u in xrange(self.number_simulations):
            deck.initialise()
            card_rules=CardRules(deck)
            card_rules.set_target(self.target_rank)

            cards_in_hand = self.get_starting_hand(deck, self.starting_cards)

            for v in range(self.number_of_draws):
                retained_cards = card_rules.apply_rules(cards_in_hand)
                #draw additional cards from deck to make a full hand
                dealer_cards = [deck.get_card() for c in
                                range(self.MAX_CARDS_IN_HAND - len(retained_cards))]
                cards_in_hand=retained_cards+dealer_cards

            # at the end of the last draw we check the final hand to see if we hit the target
            is_success=card_rules.check_success(cards_in_hand)
            if is_success:
                success_count+=1
            if self.is_plot and u>0 and u%100==0:
                self._intermediate_results.append((success_count + 0.0) / u)

        self._simulation_result = (success_count+0.0)/self.number_simulations
        return None

    def get_starting_hand(self, deck, starting_cards):
        starting_hand = []
        if(len(starting_cards)>0):
            tpcards=starting_cards.split('+')
            # do basic sanity checks
            # TODO should also add checks for suit only and rank only
            for c in tpcards:
                if(len(c)>2 or len(c)==0 or len(c)==1):
                    raise Exception('Incorrect card format. Please ensure cards are separated by `+` signs '
                                    'and are 2 characters long')
            # we assume well formatted 2 chars cards for now
            for c in tpcards:
                starting_hand.append(c)
                deck.remove_card_from_deck(c)
        # get the rest of the starting hand
        for i in range(5-starting_hand.__len__()):
            starting_hand.append(deck.get_card())
        return starting_hand

    @property
    def result(self):
        return self._simulation_result

    @property
    def intermediate_results(self):
        return self._intermediate_results




    