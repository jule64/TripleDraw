TripleDraw
========

TripleDraw is a command line tool that calculates advanced hands probabilities for the game of 2-7 Triple Draw (poker)



## Simulated vs Mathematical Probabilities

TripleDraw produces hands probabilities by **simulating** large amounts of draws and averaging all the outcomes. This technic, also called Monte Carlo simulations, allows to quickly estimate the probabilities of any type of simple or complex event scenarios found in a game of 2-7 Triple Draw. 

This flexibility however comes at the cost of precision and it is important to note that TripleDraw produces **approximate** probabilities as opposed to mathematical ones.  This means that a probability calculated by TripleDraw will be very close to the theoretical one albeit never exactly equal to it.  In practice however this trade off between precision and flexibility is usually acceptable and as a user you have control over how much precision you want as we will show in the example below.


### Example

Given that TripleDraw estimates probabilities it is worth checking how close it gets to the true mathematical probability of a given event. Suppose you wanted to know the odds of being dealt a **Jack low *pre-flop***.  The mathematical odds of this event are *9.654%(\*)*. TripleDraw by contrast gave odds of *9.804%*, *9.66%* and *9.57%* in three separate runs using the default 50,000 simulations per run. At **1 million** simulations the result becomes *9.653%*, or a *0.001%* difference only.

As you saw in this example, you can increase precision by simply increasing the number of simulations.  This however comes at a cost of longer simulation time: for instance the three 50k simulations above ran in less than a second each while the 1 million simulations took about 10 seconds(\*\*).  At the end of the day it is up to you to decide when you need higher precision depending on how closely you want to study an event.  You can easily increase precision using the `--s` parameter in the command line (see the `how to use` below for more options).  

\* Details of this calculation can be found the `study` folder in this repository.  Be warned it is quite a mouthful of equations, and that's only a simple pre-flop probability! TripleDraw allows you to study much more complex scenarios without requiring to figure out any of the complex maths underpinning those scenarios.

\*\* calculations were run on an 8 cores Macbook pro, actual performance will be dependent on your system specs.  


## Getting Started


### Installation

From your terminal window:

`git clone git@github.com:jule64/TripleDraw.git`  
`cd TripleDraw`  
`pip install --editable .`



### Run a simulation

To run the example we used earlier simply type:
`tripledraw -s ‘’ -d 0 -t J`

For more examples and help type `tripledraw --help`


## Uninstall

`pip uninstall tripledraw`


## System Requirement

TripleDraw should work on any version of **OSX** and **linux/ubuntu** that has **python 2 or 3** installed.  
If you are on Windows the installation step might be a little different but it should still work the same once installed.



## Performances

TripleDraw uses parallel processing to spread out the simulations workload among worker processes.  This allows to achieve decent sub one second performances at the default 50,000 simulations(tests ran on a MacBook with 8 virtual cores.)


If you have any questions or suggestions please feel free to contact me at jule64 at gmail dot com

If you would like to contribute please fork this project and send me a pull request.


## Next steps

1- Add small gui for entering starting cards, number of draws and number of simulations

2- Add a batch run functionality

3- add db store to save and reuse drawing stats

4- create more unit tests..


