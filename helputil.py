


def help_msgs(key):
    '''The command line `--help` command messages'''

    msgs={'starting-cards':    'Any number of predefined cards to have in your starting hand. '
                               'The default is no predefined cards (i.e. all 5 starting cards are randomly '
                               'generated on each simulation).  See example 1 and 2 printed above for details.',
          'draws':             'The number of draws to run. By default 3 which corresponds to a full hand.  '
                               'If you want to simulate a preflop scenario pass the number 0. For one draw scenario pass 1',
          'target':            'The hand you want to simulate the odds of. For example to target 8 Low simply pass 8 to this '
                               'option. The default target is J (Jack low).',
          'simulations':       'The number of simulations to run. By default it is 50,0000 which offers '
                               'roughly 0.1% precision around the true odds.',
          'procs':             'The number of parallel processes to use to run the simulations. By defaults this number is '
                               'equal to the number of cores on your machine. Set this value to 0 to run the '
                               'application single threaded.',
          'plot':              'displays a chart showing how the simulation\'s results are converging to their '
                               'final value (Parallel mode only)'}
    return msgs[key]