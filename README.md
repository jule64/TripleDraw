TripleDraw :dart:
================


**TripleDraw is a command line utility for studying cards probabilities in the game of 2-7 Triple Draw (poker)**


### Introduction

TripleDraw lets you evaluate the odds of hitting a given target hand, say 8 low, from pre-flop down to the last draw.

TripleDraw uses a technique called Monte Carlo simulations to estimate the probabilities of a given scenario.  It does that by  **simulating** large amounts of draws, apply card playing rules and average all the results into one number.  

As such it is important to note that TripleDraw is not a calculator but a simulator.  For more details about how those differ please take a look at the [Understanding TripleDraw's Results](#understanding-tripledraw-results) section.

### Installation


From your terminal window:

```
git clone git@github.com:jule64/TripleDraw.git

cd TripleDraw

pip install --editable .
```


The last step will install dependencies and create a `tripledraw` script which you can call from anywhere in your command line.

### Run a simulation

The below line checks the odds of being dealt a *Jack low pre-flop* (or better):

`tripledraw -starting-cards '' -number-of-draws 0 -target J`

This will print the result as follow  


```
starting cards | target | simulations | odds (%)
---------------|--------|-------------|---------
any            | J low  | 50000       | 9.556
```

Of course TripleDraw lets you study more advanced scenarios too, such adding one, two or three draws and specify starting cards.  The help menu shows you how to do that:  

`tripledraw --help`


### System Requirements

TripleDraw should work on any version of **OSX** and **linux/ubuntu** that has **python 2 or 3** installed.  
If you are on Windows the installation step might be a little bit different but it should still work once installed.



### Performance

TripleDraw uses parallel processing to distribute simulations load amongst worker processes.  This allows us to achieve decent sub one second performances at the default 50,000 simulations(\*).  Note Triple draw allows you set the number of worker processes for finer tuning using the `--number-procs` option.  

*(*\**) Tested on a MacBook pro with 8 virtual cores. Actual performances may vary depending on your system's specs.*



### Uninstall

`pip uninstall tripledraw`



### Understanding TripleDraw Results

The big advantage of using simulations is that it allows to evaluate complex scenarios without using complex maths, unlike you would using probabilistic calculations.
The flip side is that the results of simulations contain some degree of imprecision compared to the actual probabilities of the evaluated scenarios.  Let's look at an example to illustrate this point and see how TripleDraw minimizes this problem.


#### Example

Suppose you wanted to know the odds of being dealt a ***Jack low (or better) pre-flop***.  The mathematical approach gives this scenario a probability of *9.654%*(\*). TripleDraw by contrast gave values of *9.804%*, *9.66%* and *9.57%* in three separate runs using the default 50,000 simulations.  This gives roughly a 0.1% margin of error around the true value and the way one can interpret these results is to say *'the odds of being dealt a Jack low pre-flop are "about" 9.6%'*.  

If however you feel those results are not precise enough, you can fix that by simply increasing the number of simulations.  To take our example again we re-ran the same scenario but this time using **1 million** simulations.  The results came back as: *9.653%*, virtually the same as the actual odds.

Naturally the trade off here is that **in order to get more precision you generally have to give up computing time**.  For example, the 50k simulations above ran in under a second on my machine, whereas 1 million simulations took about 10 seconds to complete.  Note you can change these parameters by using the `-n` option, for example type `-n 500000` to run five hundred thousand simulations.


(\*)*By the way if you want to know how this number is calculated have a look in the `study` folder where I have added all the calculations step by step. Needless to say it's a lot of equations, and that's only for a simple pre-flop probability.  By contrast the simulations-style approach of TripleDraw means no complex maths are required :)*


### Finally


If you have any questions or suggestions please feel free to raise an issue or contact me at jule64 at gmail dot com.

If you would like to contribute please fork this project and send me a pull request.



:hearts: :spades: :diamonds: :clubs: :hearts: :spades: :diamonds: :clubs: :hearts: :spades: :diamonds: :clubs: :hearts: :spades: :diamonds: :clubs: :hearts: :spades: :diamonds: :clubs: :hearts:
