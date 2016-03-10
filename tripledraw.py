import datetime
import math
import click
import plotutil
from colors import red, blue
from multiprocessing import Process, Queue, cpu_count
from simulation import Simulation
from helputil import help_msgs


@click.command()
@click.option('--starting-cards','-s', prompt=True, default='', help=help_msgs('starting-cards'))
@click.option('--draws','-d', prompt=True, default=0, help=help_msgs('draws'))
@click.option('--target', '-t', prompt=True, default='J', help=help_msgs('target'))
@click.option('--simulations','-n', default=100000, help=help_msgs('simulations'))
@click.option('--procs','-p', default=cpu_count()-1, help=help_msgs('procs'))
@click.option('--plot', is_flag=True, help=help_msgs('plot'))
def main(starting_cards, draws, target, simulations, procs, plot):
    """Welcome to tripledraw!

    ## usage examples:

    1. (verbose use):    `tripledraw --starting-cards Ks+Jc+8 --number-of-draws 1 --target 9`

    2. (condensed use):  `tripledraw -s K*+10s+Jd -d 3 -t 10`

    Note use `*` to mean 'any' in your starting hand. For instance K* in
    example 2 above means 'any Kings'.  KJ* means any Kings or Jacks

    **************************************************************************
    """

    s = SimulationManager(starting_cards, draws, target, simulations, procs, plot)
    s.run_simulation()


class SimulationManager:

    def __init__(self, *args):
        self.starting_cards, self.draws, self.target, self.simulations, self.procs, self.plot = args
        self.result = None
        self.plot_list = None

    def run_simulation(self):
        if self.starting_cards != '' and self.draws == 0:
            print red('>>> Warning: you are using starting card(s) with 0 draws.  '
                      'You should use at least one draw when you provide starting cards')
        if self.procs <= 1:
            self.run_single_threaded()
        else:
            self.run_parallel()

    def run_single_threaded(self):
        print "Running {:,} simulations (single threaded mode)".format(self.simulations)
        simulation = Simulation(self.starting_cards, self.draws, self.target, self.simulations, self.plot)
        exec_start = datetime.datetime.now()
        if self.plot:
            print red('>>> Info: no charting available in single threaded mode')
        simulation.launch()
        result = simulation.result()
        exec_time=datetime.datetime.now()-exec_start
        self.report_results_to_stdout(result, exec_time)

    def run_parallel(self):

        def runner(queue, simulation, plot):
            simulation.launch()
            result = simulation.result
            if plot:
                plot_data = simulation.intermediate_results
                queue.put([result, plot_data])
            else:
                queue.put(result)

        print 'Running {:,} simulations using {} parallel workers'.format(self.simulations, self.procs)
        simulations_per_proc= (self.simulations - self.simulations % self.procs) / self.procs
        print 'Each parallel worker will process {} simulations'.format(simulations_per_proc)

        exec_start = datetime.datetime.now()
        q = Queue()
        jobs = []
        for i in range(self.procs):
            simulation = Simulation(self.starting_cards, self.draws, self.target, simulations_per_proc, self.plot)
            p = Process(target=runner, args=(q, simulation, self.plot))
            jobs.append(p)
            p.start()

        # ensuring all the parallel processes finish running
        for p in jobs:
            p.join()

        proc_results=[]
        plot_data=[]
        while not q.empty():
            if self.plot:
                _res=q.get()
                proc_results.append(_res[0])
                plot_data.append(_res[1])
            else:
                proc_results.append(q.get())
        exec_time=datetime.datetime.now()-exec_start

        # the final result reported to the command line
        aggregated_result = math.fsum(proc_results) / self.procs
        self.report_results_to_stdout(aggregated_result, exec_time)

        if self.plot:
            plotutil.plot_simulation_results(plot_data, self.simulations, self.procs)

    def report_results_to_stdout(self, result, exec_time):
        """pretty prints the results of a simulation"""

        print blue('Execution time: {}s {}ms'.format(exec_time.seconds,exec_time.microseconds))

        if self.starting_cards == '':
            self.starting_cards='any'

        result_record=[self.starting_cards, str(self.draws), self.target + ' low', '{:,}'.format(self.simulations), '{0:.4%}'.format(result)]
        headers = ['starting cards','nb draws','target hand','simulations','odds (%)']
        collist = tuple([i for i in range(headers.__len__() + 1)])
        # this sets the initial column width based on the width of the headers
        colwidth = dict(zip(collist,(len(str(x)) for x in headers)))
        # if the width of our values is longer than the corresponding header's we update that column's width
        colwidth.update(( i, max(colwidth[i],len(el)) ) for i,el in enumerate(result_record))
        width_pattern = ' | '.join('%%-%ss' % colwidth[i] for i in xrange(0,5))

        # note the lists are converted into tuples in order to apply width_pattern onto them
        print '\n','\n'.join((width_pattern % tuple(headers),'-|-'.join( colwidth[i]*'-' for i in xrange(5)),''.join(width_pattern % tuple(result_record))))


if __name__ == '__main__':
    # The below is used for dev.  The `default_map` object gets passed to Click to set the defaults.
    # This avoids messing about with the defaults in the Click decorators in main()
    main(default_map={
        'simulations': 10000,
        'procs':3,
        'draws':1,
        'starting_cards':'',
        'target':'8',
        'plot':True,
    })


