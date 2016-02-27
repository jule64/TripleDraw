TripleDraw :dart:
================

  
  
**TripleDraw is a command line utility for studying cards probabilities in the game of 2-7 Triple Draw (poker)**



☤ Simulations vs Mathematical Probabilities
-----------------------------------------

TripleDraw uses a technique called Monte Carlo simulations to estimate the probabilities of an event.  It does this by  **simulating** large amounts of draws, apply card playing rules and average all the results into one number.  
While this allows TripleDraw to handle a vast array of complex game scenarios, simulations come with some degrees of imprecision when compared to the exact theoretical odds of an event, although in practice those diffrences are very small and configurable.  To illustrate this point let’s look at an example.


A Simulation Example
~~~~~~~~~~~~~~~~

Suppose you wanted to know the odds of being dealt a **Jack low** ***pre-flop***.  The mathematical probabilities of this event are *9.654%* (\*). TripleDraw by contrast gave values of *9.804%*, *9.66%* and *9.57%* in three separate runs of 50,000 simulations per run. Using **1 million** simulations the result becomes *9.653%*, which is virtually the same as the mathematical values.


Precision factor
~~~~~~~~~~~~~~~~

As this example shows, you can get closer to the true odds of an event by simply increasing the number of simulations.  Doing so however comes at a cost of longer simulation time: for instance 50k simulations run in less than 1 second, a very acceptable time. For 1 million simulations however you are looking at a running time of about 10 seconds(**).  Note that you can tune the precision to your desired level by using the `-n` parameter in the command line.

(*) Details of this calculation can be found the `study` folder in this repository.  Be warned it is quite a mouthful of calculations, and that's only for a simple pre-flop probability! **TripleDraw allows you to study much more complex scenarios without requiring to figure out any of the complex maths underpinning those scenarios**.

(**) calculations were run on an 8 cores Macbook pro, actual performance will be dependent on your system specs.  


☤ Getting Started
-----------------

Installation
~~~~~~~~~~~~

From your terminal window:

``git clone git@github.com:jule64/TripleDraw.git`` 

``cd TripleDraw``  

``pip install --editable .``


The last step will install dependencies if they are missing and create an executable script which you can call from anywhere in your command line.

Run a simulation
~~~~~~~~~~~~~~~~

To run the example we used earlier type:  

``tripledraw -s '' -d 0 -t J``

This will print the result as follow  

.. code:: pycon:

    starting cards | target | simulations | odds (%)
    ---------------|--------|-------------|---------
    any            | J low  | 50000       | 9.556



For more usage examples and commands descripitons:  

``tripledraw --help``


Uninstall
~~~~~~~~~~

``pip uninstall tripledraw``


System Requirement
~~~~~~~~~~~~~~~~~~~

TripleDraw should work on any version of **OSX** and **linux/ubuntu** that has **python 2 or 3** installed.  
If you are on Windows the installation step might be a little bit different but it should still work once installed.



Performance
~~~~~~~~~~~~~

TripleDraw uses parallel processing to spread out the simulations workload among worker processes.  This allows to achieve decent sub one second performances at the default 50,000 simulations(tests ran on a MacBook with 8 virtual cores.)


If you have any questions or suggestions please feel free to contact me at jule64 at gmail dot com

If you would like to contribute please fork this project and send me a pull request.




☤ Next steps
------------

1 Add small gui for entering starting cards, number of draws and number of simulations

2 Add a batch run functionality

3 add db store to save and reuse drawing stats

4 create more unit tests



