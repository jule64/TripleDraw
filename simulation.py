import datetime
import math
from multiprocessing import Queue, Process, process
from colors import red, blue
import plotutil
from cardrules import CardRules
from deck import Deck
import logging
from concurrent.futures import ProcessPoolExecutor


class Simulation(object):
    '''
    The main simulation object
    '''

    def __init__(self,starting_cards=None, number_draws=None, target=None, simulations=None,
                 plot=None, collect_frequency=None):

        self.starting_cards=starting_cards
        self.number_of_draws=number_draws
        self.target_rank=target
        self.number_simulations=simulations
        self.is_plot = plot
        self.MAX_CARDS_IN_HAND=5
        self._intermediate_results = []
        self._simulation_result = None
        self.collect_frequency = collect_frequency

    def launch(self, proc_number):
        '''
        Runs a simulation
        :return: double: the ratio of successful hands over total hands
        '''

        logging.info(process.current_process().name + ': Plot data will be collected every {} runs'.
                     format(self.collect_frequency))

        success_count = 0
        deck = Deck()

        for sim_nb in range(self.number_simulations):
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
                success_count += 1
            if self.is_plot and sim_nb % self.collect_frequency == 0 and sim_nb > 0:
                self._intermediate_results.append((success_count) / sim_nb)

        self._simulation_result = (success_count)/self.number_simulations
        return self

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


class SimulationManager:

    def __init__(self, *args):
        self.starting_cards, self.draws, self.target, self.simulations, self.procs, self.plot = args
        self.result = None
        self.plot_list = None

    def run_simulation(self):
        if self.starting_cards != '' and self.draws == 0:
            print(red('>>> Warning: you are using starting card(s) with 0 draws.  '
                      'You should use at least one draw when you provide starting cards'))

        if self.simulations < 1000:
            print(red('>>> Error: please choose a number of simulations greater than 1,000'))
            return None

        self.procs = 1 if self.procs <= 1 else self.procs

        print('Running {:,} simulations using {} workers'.format(self.simulations, self.procs))
        simulations_per_proc = (self.simulations - self.simulations % self.procs) // self.procs
        print('Each worker will process {:,} simulations'.format(simulations_per_proc))

        exec_start = datetime.datetime.now()

        plot_data=[]
        proc_results=[]
        with ProcessPoolExecutor() as executor:
            for simulation in executor.map(Simulation(self.starting_cards, self.draws, self.target, simulations_per_proc, self.plot
                    , plotutil.collect_frequency(self.simulations)).launch, range(self.procs)):
                proc_results.append(simulation.result)
                plot_data.append(simulation.intermediate_results)

        exec_time=datetime.datetime.now()-exec_start

        # the final result reported to the command line
        aggregated_result = math.fsum(proc_results) / self.procs
        self.report_results_to_stdout(aggregated_result, exec_time)

        if self.plot:
            plotutil.plot_simulation_results(plot_data, self.simulations, self.procs)

    def report_results_to_stdout(self, result, exec_time):
        """pretty prints the results of a simulation"""

        print(blue('Execution time: {}s {}ms'.format(exec_time.seconds, exec_time.microseconds)))

        if self.starting_cards == '':
            self.starting_cards='any'

        result_record=[self.starting_cards, str(self.draws), self.target + ' low', '{:,}'.format(self.simulations), '{0:.4%}'.format(result)]
        headers = ['starting cards','nb draws','target hand','simulations','odds (%)']
        collist = tuple([i for i in range(headers.__len__() + 1)])
        # this sets the initial column width based on the width of the headers
        colwidth = dict(zip(collist,(len(x) for x in headers)))
        # if the width of our values is longer than the corresponding header's we update that column's width
        colwidth.update(( i, max(colwidth[i],len(el)) ) for i,el in enumerate(result_record))
        width_pattern = ' | '.join('%%-%ss' % colwidth[i] for i in range(0,5))

        # note the lists are converted into tuples in order to apply width_pattern onto them
        print('\n'.join((width_pattern % tuple(headers), '-|-'.join(colwidth[i] * '-' for i in range(5)),
                               ''.join(width_pattern % tuple(result_record)))))
