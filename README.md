TripleDraw :dart:
================


**TripleDraw is a command line utility for studying cards probabilities in the games of 2-7 Triple Draw And Single Draw (poker)**


### Background Info
I created this project primarily to brush up my Python programming skills and learn to manage an open source project end to end.  It is free to use however I do not provide guarantees as to the accuracy of the tool.  See also [disclaimer](#diclaimer) section below.


### Introduction

TripleDraw lets you evaluate the odds of hitting a given target hand, say 8 low, from *pre-flop stage* to the *last draw* stage.

TripleDraw uses a technique called Monte Carlo simulations to estimate the probabilities of a given scenario.  It does that by  **simulating** large amounts of random draws, apply card playing rules and average out the results.  

As such it is important to note that TripleDraw is not a calculator but a *simulator*.  You can find more details about how those compare in the [Understanding TripleDraw's Results](#understanding-tripledraw-results) section.

### Installation


From your terminal window:

```
git clone git@github.com:jule64/TripleDraw.git

cd TripleDraw

pip install --editable .
```


The last step will install dependencies and create a `tripledraw` script which you can call from anywhere in your command line.

### Run a simulation

The below line will evaluate the odds of being dealt a *Jack low (or better) pre-flop*:

`tripledraw -starting-cards '' -number-of-draws 0 -target J`

This will print the result as follow  


```
starting cards | nb draws | target hand | simulations | odds (%) 
---------------|----------|-------------|-------------|----------
any            | 0        | J low       | 150,000     | 9.692667%   
```

Of course you can also study more advanced scenaarios, such adding one, two or three draws and specify starting cards. **In fact setting the number of draws to 1 allows you to study the single draw variant of the game!**  

The help menu shows you how to run simulations in more details:  

`tripledraw --help`


### System Requirements

TripleDraw should work on any version of **OSX** and **linux/ubuntu** with **python 2 or 3** installed.  
If you are on Windows the installation step might be a little different but it should still work once installed.



### Performance

TripleDraw uses parallel processing to distribute the simulations amongst worker processes.  This allows us to achieve decent sub second performances at the default 50,000 simulations(\*).  You can set the number of worker processes manually using the `--number-procs` option.  

*(*\**) Tested on a MacBook pro with 8 virtual cores. Actual performances may vary depending on your system's specs.*



### Uninstall

`pip uninstall tripledraw`



### Understanding TripleDraw Results

The big advantage of using simulations is that it allows to evaluate complex scenarios without using complex maths, unlike you would using probabilistic calculations.
The flip side is that simulations contain some degree of imprecision compared to the actual probabilities of the evaluated scenarios.  Let's look at an example to illustrate this point and see how to minize this problem with TripleDraw.


#### Example

Suppose you wanted to know the odds of being dealt a ***Jack low (or better) pre-flop***.  The mathematical approach gives this scenario a probability of *9.654%*(\*). TripleDraw by contrast gave values of *9.804%*, *9.66%* and *9.57%* in three separate runs using the default 50,000 simulations, roughly a 0.1% precision around the true value.  Since there is no real advantage in using odds beyond one decimal place in poker, the way one could read these results is to say *'the odds of being dealt a Jack low pre-flop are "about" 10%'*.  

If however you feel those results are too "wide", you can fix that by simply increasing the number of simulations.  To take our example again we re-ran the same scenario but this time using **1 million** simulations.  The results came back as: *9.653%*, virtually the same as the actual odds.

The trade off hence is that *in order to get more precision you generally have to give up computing time*.  For instance, the 50k simulations above ran in under a second on my machine, whereas 1 million simulations took about 10 seconds to complete.  You can change the default number of simulations with the `-n` option, for example `-n 500000` to run five hundred thousand simulations.


(\*)*By the way if you want to know how this number is calculated have a look in the `study` folder where I have added all the calculations step by step. Needless to say it's a lot of equations, and that's only for a simple pre-flop probability.  By contrast the simulations-style approach of TripleDraw means no complex maths are required :)*


### Finally


If you have any questions or suggestions please feel free to raise an issue or contact me at jule64 at gmail dot com.

Contributions are welcome!


### DISCLAIMER
Copyright (c) 2016 by Julien Monnier and contributors.

THIS SOFTWARE AND DOCUMENTATION IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE AND DOCUMENTATION, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.