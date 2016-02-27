TripleDraw
========

TripleDraw is a command line tool that helps you calculate drawing probabilities for the game of 2-7 Triple Draw (poker)
  



## Simulated vs Mathematical Probabilities

TripleDraw produces drawing probabilities by **simulating** large amounts of draws and averaging all the outcomes. This technic, also called Monte Carlo simulations, allows TripleDraw to quickly estimate the probabilities of complex events found in a game of 2-7 Triple Draw while not having to model the complex probabilitic rules of those events. 

This flexibility however comes at the cost of precision and it is important to note that TripleDraw produces **approximate** probabilities as opposed to mathematical ones.  This means that a probability calculated by TripleDraw will be close to the theoretical one albeit never exactly equal to it.  In practice however this trade off between precision and flexibilty is usually acceptable and as a user you are also able to decide how much precision you want as we will show in the example below.


### Example

Given that TripleDraw is a simulator it is worth to check how close it gets to the true mathematical probability of a given event. Suppose you wanted to know the odds of being dealt a Jack low *pre-flop*.  The mathematical odds of this event are 9.65%(\*). TripleDraw by contrast gave odds of 9.804%, 9.66% and 9.57% in three separate runs using the default 50,000 simulations per run. At **1 million** simulations the result becomes 9.653%, pretty much the same as the mathematical odds.  

As you saw in this example, you can increase precision by simply increasing number of simulations.  This however comes at a cost of longer simulation time: 50k simulations ran in less than a second while 1 million simulations took about 10 seconds(\*\*) .  At the end of the day it is up to you to decide when you need higher precision depending on how closely you want to study an event.  You can easily increase precision using the `--s` parameter in the command line (see how to use below for more options).  

\* You can view the calculations behind this number in the `study` folder in this repository.  Be warned it is quite a mouthful of calculations, and that's only a simple pre-flop probability! TripleDraw allows you to study much more complex scenarios without doing any of the complex maths that come with them.  

\*\* calculations were run on an 8 cores Macbook pro, actual performance will be dependent on your system specs.

## How to use

Currently TripleDraw runs in a command line mode only.  We aim to bring UI in the next release.


## Performances

The current version of TripleDraw has an average processing time of 7 seconds per 50,000 simulations, which is rather slow but nevertheless an improvement from 13 seconds of the initial unreleased version.  We will attempt to bring down the processing time under 1 second in the next release (see ‘next steps’ section below).

## Versionning

Current release of TripleDraw is 1.0. 

TripleDraw has been developed and tested on a Mac OSX using a Python 2.7 interpreter. It should however run normaly on any os that has Python installed.


If you have any questions or suggestions please feel free to contact me. 

If you would like to contribute please fork this project.


## Next steps

1- Add small gui for entering starting cards, number of draws and number of simul

2- add db store to save and reuse drawing stats

3- Improve simulation runtime performance (see profiler notes)
