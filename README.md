SimuDraw
========

SimuDraw is an odds simulator for the game of 2-7 Triple Draw


## Background Info

Despite being one of the hottest games in online poker, 2-7 Triple Draw lacks badly of online resources and free tools to help players improve their game.

SimuDraw tries to fill this gap by providing players a virtual environment for studying various hands/game configurations and their associated odds.


## How it works

SimuDraw produces drawing statistics by simulating a large amount of random draws and averaging their results.  As such please note that SimuDraw does not provide exact *mathematical* drawing odds but instead close approximations of the actual odds.

### Example
As an example, suppose you wanted to know the odds of being dealt a Jack low *pre-flop*.  
The mathematical odds of this event are 4.905% (C(9,4)*(5^4-4)/C(52,5)). 
By contrast SimuDraw gives probabilities in the range of 4.87% to 4.95% using the default 50,000 simulations per run, equivalent to a 0.1% precision.  That difference becomes less than 0.01% with 200k simulations per run.

## How to use

Currently SimuDraw runs in a command line mode only.  We aim to bring UI in the next release.


## Performances

The current version of SimuDraw has an average processing time of 7 seconds per 50,000 simulations, which is rather slow but nevertheless an improvement from 13 seconds of the initial unreleased version.  We will attempt to bring down the processing time under 1 second in the next release (see ‘next steps’ section below).

## Versionning

Current release of SimuDraw is 1.0. 

SimuDraw has been developed and tested on a Mac OSX using a Python 2.7 interpreter. It should however run normaly on any os that has Python installed.


If you have any questions or suggestions please feel free to contact me. 

If you would like to contribute please fork this project.


## Next steps

1- Add small gui for entering starting cards, number of draws and number of simul

2- add db store to save and reuse drawing stats

3- Improve simulation runtime performance (see profiler notes)
