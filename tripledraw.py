
from multiprocessing import Process, Queue, cpu_count
import click
from simulation import SimulationBuilder
import math
import logging
from colors import red


help_msgs={'starting-cards':    'Any number of predefined cards to have in your starting hand. '
                                'The default is no predefined cards (i.e. all 5 starting cards are randomly '
                                'generated on each simulation).  See example 1 and 2 printed above for details.',
           'number-of-draws':   'The number of draws to simulate. By default 3 which corresponds to a full hand.  '
                                'If you want to simulate a late stage, for example when there is only one draw left, '
                                'simply pass the number 1.  Use 0 to simulate preflop stage, useful if for example '
                                'you want to know the odds of being dealt a 10 low pre flop.',
           'target':            'The hand you want to simulate the odds of. For example to target 8 Low simply pass 8 to this '
                                'option. The default target is J (Jack low).',
           'simulations':       'The number of simulations to run. By default it is 50,0000 which offers '
                                'roughly 0.1% precision around the true odds.',
           'number-procs':      'The number of parallel processes used to run the simulations. By defaults this number is '
                                'equal to the number of cores available on your machine. Set this value to 0 to run the '
                                'application single threaded.'
           }


# logger setup
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tripledraw')
logger.setLevel(logging.INFO)



@click.command()
@click.option('--starting-cards','-s', prompt=True, default='', help=help_msgs['starting-cards'])
@click.option('--number-of-draws','-d', prompt=True, default=0, help=help_msgs['number-of-draws'])
@click.option('--target', '-t', prompt=True, default='J',
              help=help_msgs['target'])
@click.option('--simulations','-n', default=50000,
              help=help_msgs['simulations'])
@click.option('--number-procs','-p', default=cpu_count(),
              help=help_msgs['number-procs'])
def main(starting_cards, number_of_draws, target, simulations, number_procs):

    """Welcome to tripledraw!


    ## usage examples:

    1. (verbose use):    `tripledraw --starting-cards Ks+Jc+8 --number-of-draws 1 --target 9`

    2. (condensed use):  `tripledraw -s K*+10s+Jd -d 3 -t 10`

    Note use `*` to mean 'any' in your starting hand. For instance K* in
    example 2 above means 'any Kings'.  KJ* means any Kings or Jacks

    **************************************************************************
    """
    # if(starting_cards != ''):
    #     print '[!] Simulation Aborted:  Adding starting cards is not currently supported.  Apologies'
    #     return
    # if(target!='J'):
    #     print "[!] Simulation Aborted:  Only Jack low target (J) is currently supported.  Apologies"
    #     return

    if(starting_cards <> '' and number_of_draws==0):
        print red('>>> Warning: you are using starting card(s) with 0 draws.  '
                  'You should use at least one draw when you provide starting cards')



    if(number_procs<=1):
        run_single_threaded(starting_cards, number_of_draws, target, simulations)
    else:
        run_multi_procs(starting_cards, number_of_draws, target, simulations, number_procs)


def run_single_threaded(starting_cards, number_of_draws, target, simulations):
    print "Running {} simulations into a single thread".format(simulations)
    simulator = build_simulator(starting_cards, number_of_draws, target, simulations)
    result = simulator.launch()
    report_results(starting_cards, target, simulations, result)


def run_multi_procs(starting_cards, number_of_draws, target, simulations, numberProcs):
    # logger.info('Dispatching %s simulations to %s parallel workers',simulations, numberProcs)
    print 'Dispatching {} simulations to {} parallel workers'.format(simulations, numberProcs)
    simulationsPerProcs= (simulations - simulations % numberProcs) / numberProcs
    print 'Each parallel worker will process %s simulations'.format(simulationsPerProcs)

    q = Queue()
    jobs = []
    for i in range(numberProcs):
        simulator = build_simulator(starting_cards, number_of_draws, target, simulationsPerProcs)

        p = Process(target=runner, args=(q,simulator))
        jobs.append(p)
        p.start()

    # ensuring all the processes finish running
    for p in jobs:
        p.join()

    procsResults=[]
    while not q.empty():
        procsResults.append(q.get())

    mergedResults = math.fsum(procsResults) / numberProcs

    report_results(starting_cards, target, simulations, mergedResults)


def runner(queue,simulator):
    result = simulator.launch()
    queue.put(result)


def report_results(starting_cards, target, simulations, results):
    # pretty prints the results

    results_percent=results * 100

    result_record=[starting_cards,target+' low',str(simulations),str(results_percent)]
    headers = ['starting cards','target','simulations','odds (%)']
    collist = tuple([i for i in range(headers.__len__() + 1)])
    # this sets the initial column width based on the width of the headers
    colwidth = dict(zip(collist,(len(str(x)) for x in headers)))
    # if the width of our values is longer than the corresponding header's we update that column's width
    colwidth.update(( i, max(colwidth[i],len(el)) ) for i,el in enumerate(result_record))
    width_pattern = ' | '.join('%%-%ss' % colwidth[i] for i in xrange(0,4))

    # note the lists are converted into tuples in order to apply width_pattern onto them
    print '\n','\n'.join((width_pattern % tuple(headers),'-|-'.join( colwidth[i]*'-' for i in xrange(4)),''.join(width_pattern % tuple(result_record))))



def build_simulator(starting_cards, number_of_draws, target, simulations):
    return SimulationBuilder() \
        .setStartingCards(starting_cards) \
        .setNumberOfDraws(number_of_draws) \
        .setTarget(target) \
        .setSimulations(simulations) \
        .build()


if __name__ == '__main__':

    # The below is used for dev.  The object gets passed to Click to set the defaults. This avoids messing about with
    # the defaults in the decorators setup in main()
    main(default_map={
        'simulations': 1000,
        'number_procs':0,
        'number_of_draws':0,
        'starting_cards':'',
        'target':'A'
    })

