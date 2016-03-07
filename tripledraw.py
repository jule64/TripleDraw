from multiprocessing import Process, Queue, cpu_count
import click
import datetime
import plot
from simulation import SimulationBuilder
import math
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
                                'application single threaded.',
           'plot':              'True/False:  plots a graph of how the odds are converging to their final value.'
           }

@click.command()
@click.option('--starting-cards','-s', prompt=True, default='', help=help_msgs['starting-cards'])
@click.option('--number-of-draws','-d', prompt=True, default=0, help=help_msgs['number-of-draws'])
@click.option('--target', '-t', prompt=True, default='J',
              help=help_msgs['target'])
@click.option('--simulations','-n', default=100000,
              help=help_msgs['simulations'])
@click.option('--number-procs','-p', default=cpu_count(),
              help=help_msgs['number-procs'])
@click.option('--plot','-p', type=bool, default=False,
              help=help_msgs['plot'])
def main(starting_cards, number_of_draws, target, simulations, number_procs, plot):

    """Welcome to tripledraw!

    ## usage examples:

    1. (verbose use):    `tripledraw --starting-cards Ks+Jc+8 --number-of-draws 1 --target 9`

    2. (condensed use):  `tripledraw -s K*+10s+Jd -d 3 -t 10`

    Note use `*` to mean 'any' in your starting hand. For instance K* in
    example 2 above means 'any Kings'.  KJ* means any Kings or Jacks

    **************************************************************************
    """

    if(starting_cards <> '' and number_of_draws==0):
        print red('>>> Warning: you are using starting card(s) with 0 draws.  '
                  'You should use at least one draw when you provide starting cards')

    exec_start_time = datetime.datetime.now()
    if(number_procs<=1):
        run_single_threaded(starting_cards, number_of_draws, target, simulations,plot,exec_start_time)
    else:
        run_multi_procs(starting_cards, number_of_draws, target, simulations, number_procs, plot,exec_start_time)

def run_single_threaded(starting_cards, number_of_draws, target, simulations,is_plot,exec_start_time):
    print "Running {:,} simulations (single threaded mode)".format(simulations)
    simulator = build_simulator(starting_cards, number_of_draws, target, simulations,is_plot)
    if is_plot:
        print red('>>> Warning: no charting available in single threaded mode')
        result, plot_list = simulator.launch()
    else:
        result = simulator.launch()
    exec_time=datetime.datetime.now()-exec_start_time
    report_results(starting_cards, number_of_draws, target, simulations, result,exec_time)

def run_multi_procs(starting_cards, number_of_draws, target, simulations, numberProcs, is_plot,exec_start_time):
    # logger.info('Dispatching %s simulations to %s parallel workers',simulations, numberProcs)
    print 'Running {:,} simulations using {} parallel workers'.format(simulations, numberProcs)
    simulationsPerProcs= (simulations - simulations % numberProcs) / numberProcs
    print 'Each parallel worker will process {} simulations'.format(simulationsPerProcs)

    q = Queue()
    jobs = []
    for i in range(numberProcs):
        simulator = build_simulator(starting_cards, number_of_draws, target, simulationsPerProcs,is_plot)
        p = Process(target=runner, args=(q,simulator,is_plot))
        jobs.append(p)
        p.start()

    # ensuring all the processes finish running
    for p in jobs:
        p.join()

    procsResults=[]
    plotResults=[]
    while not q.empty():
        if(is_plot):
            _res=q.get()
            procsResults.append(_res[0])
            plotResults.append(_res[1])
        else:
            procsResults.append(q.get())
    exec_time=datetime.datetime.now()-exec_start_time

    mergedResults = math.fsum(procsResults) / numberProcs
    report_results(starting_cards, number_of_draws, target, simulations, mergedResults, exec_time)

    if(is_plot):
        plot.plot_simulation_results(plotResults,simulations,numberProcs)


def runner(queue,simulator,is_plot):
    if is_plot:
        result, plots = simulator.launch()
        queue.put([result,plots])
    else:
        result = simulator.launch()
        queue.put(result)

def report_results(starting_cards, number_of_draws, target, simulations, results,exec_time):
    '''pretty prints the results of a simulation
    '''
    print 'execution time: {}s {}ms'.format(exec_time.seconds,exec_time.microseconds)

    result_record=[starting_cards,str(number_of_draws), target+' low','{:,}'.format(simulations),'{0:.4%}'.format(results)]
    headers = ['starting cards','nb draws','target hand','simulations','odds (%)']
    collist = tuple([i for i in range(headers.__len__() + 1)])
    # this sets the initial column width based on the width of the headers
    colwidth = dict(zip(collist,(len(str(x)) for x in headers)))
    # if the width of our values is longer than the corresponding header's we update that column's width
    colwidth.update(( i, max(colwidth[i],len(el)) ) for i,el in enumerate(result_record))
    width_pattern = ' | '.join('%%-%ss' % colwidth[i] for i in xrange(0,5))

    # note the lists are converted into tuples in order to apply width_pattern onto them
    print '\n','\n'.join((width_pattern % tuple(headers),'-|-'.join( colwidth[i]*'-' for i in xrange(5)),''.join(width_pattern % tuple(result_record))))

def build_simulator(starting_cards, number_of_draws, target, simulations,is_plot):
    return SimulationBuilder() \
        .set_starting_cards(starting_cards) \
        .set_number_of_draws(number_of_draws) \
        .set_target(target) \
        .set_simulations(simulations) \
        .set_plot(is_plot) \
        .build()

if __name__ == '__main__':

    # The below is used for dev.  The object gets passed to Click to set the defaults. This avoids messing about with
    # the defaults in the decorators setup in main()
    main(default_map={
        'simulations': 150000,
        'number_procs':4,
        'number_of_draws':0,
        'starting_cards':'',
        'target':'7',
        'plot':True,
    })

# # logger setup
# FORMAT = '%(asctime)-15s %(message)s'
# logging.basicConfig(format=FORMAT)
# logger = logging.getLogger('tripledraw')
# logger.setLevel(logging.INFO)
