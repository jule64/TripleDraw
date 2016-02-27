TripleDraw
========

TripleDraw is a tool for calculating drawing probabilities for the game of 2-7 Triple Draw (poker)



## Intro

TripleDraw produces drawing probabilities by simulating large amounts of draws and averaging the results.  In doing so, TripleDraw is able to closely *approximate* the true probabilities of a an event without doing any complex calculations.  

So why not calculating actual probabilities you might ask?  Because the maths behind the game of 2-7 Triple Draw are far too complex and numerous to figure out due to the presence of drawing stages and the option to discard (or not discarded) cards at each stage.  By contrast, TripleDraw is able to calculate ANY probabalities without knowing about the maths of the events it is requested to calculate. This flexibility however come at the cost of a small degree of imprecision which in practice however is small and acceptable as we will show below.


## Simulated vs Mathematical Probabilities

Given TripleDraw is a simulator let's look at an example to see how it compares in real life. Suppose you wanted to know the odds of being dealt a Jack low *pre-flop*.  The mathematical odds of this event are 9.65%. With TripleDraw the results where 9.804%, 9.66% and 9.57% in three separate runs and using the default 50,000 simulations per run. At 1 million simulations the number becomes 9.653%, almost imperciptible from the actual odds.  Naturally precision comes at a cost of more sumlations and hence longer simulation time: 50k simulations run in under a second, 1million simulations take about 10 seconds.  At the end of the day it is up to you to decide when you need higher precision depending on how closely you want to study an event.  You can easily increase precision from the command line as we will show below.  

Oh and in case you wonder how I obtained the mathematical odds in the example above (since I needed a reference point to compare TripleDraw against), you can find the answer in the `study` folder in this repository.  Be warned it is quite a mouthful of calculations, and that's only a simple pre-flop probability!


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
