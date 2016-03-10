from multiprocessing import cpu_count

import click

from helputil import help_msgs
from simulation import SimulationManager


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


