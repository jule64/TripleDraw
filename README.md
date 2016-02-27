TripleDraw
========

TripleDraw is a command line tool to study advanced hands probabilities for the game of 2-7 Triple Draw (poker)



## Simulated vs Mathematical Probabilities

TripleDraw uses a technique called Monte Carlo simulations which allows it to evaluate any types of complex scenarios by **simulating** large amounts of draws and averaging the outcomes.

While simulations are a flexible and powerful way to estimate the probabilities of complex events, it is important to note that this comes at a cost of some imprecision in the results.  Indeed because it is a simulator, TripleDraw’s results will be very close to the theoretical values of a given event albeit never exactly equal to it.  To illustrate this point let’s look at an example.


### Example

TripleDraw provides estimations of mathematical probabilities, as such it is worth checking how close it gets to the actual values of a given event.  As an example suppose you wanted to know the odds of being dealt a **Jack low** ***pre-flop***.  The mathematical odds of this event are *9.654%* (\*). TripleDraw by contrast gave values of *9.804%*, *9.66%* and *9.57%* in three separate runs of 50,000 simulations per run. At **1 million** simulations the result becomes *9.653%*, which is virtually equal to the mathematical value.

As you saw in the example above, you can get closer to the true value of an event by simply increasing the number of simulations.  Doing so however comes at a cost of longer simulation time: for instance 50k simulations run in less than 1 second, a very acceptable time. For 1 million simulations on the other hand this goes to 10 seconds(**).  Note that you can set the number of simulations you want to run by using the `-n` parameter in the command line which allows you to easily increase or decrease precision as required.

(*) Details of this calculation can be found the `study` folder in this repository.  Be warned it is quite a mouthful of equations, and that's only a simple pre-flop probability! TripleDraw allows you to study much more complex scenarios without requiring to figure out any of the complex maths underpinning those scenarios.

(**) calculations were run on an 8 cores Macbook pro, actual performance will be dependent on your system specs.  


## Getting Started


### Installation

From your terminal window:

`git clone git@github.com:jule64/TripleDraw.git`  
`cd TripleDraw`  
`pip install --editable .`



### Run a simulation

To run the example we used earlier simply type:  
`tripledraw -s '' -d 0 -t J`

For more examples and help type:  
`tripledraw --help`


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


