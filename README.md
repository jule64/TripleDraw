SimuDraw
========

SimuDraw is an odds simulator for the game of 2-7 Triple Draw


## Background Info

Despite being one of the hottest games in online poker, there are few tools available out there for 2-7 Triple Draw players who want to improve their game.

SimuDraw tries to remedy this problem by providing a virtual environment where players can study the outcome of various hands/game configurations and their associated odds.


## How it works

SimuDraw produces its results by simulating a large amount of draws and averaging the results of those draws.  As such please note that SimuDraw does not provide exact odds but instead approximations of the actual odds.

To illustrate the difference, suppose you wanted to know what the chances are of being dealt a J low pre-flop.  The odds of this event are 4.905% and are given by the following formula: C(9,4)*(5^4-4)/C(52,5)) = 4.9%. By contrast SimuDraw gave a result of 4.87% and 4.95% on two separate runs of 50,000 simulations each, giving a precision of roughly 0.1% away from the actual value.  That difference becomes less than 0.01% with 200k simulations per run.


## Performances

The current version of SimuDraw (1.0) has an average processing time of 7 seconds per 50,000 simulations, down from 13 seconds for the initial unrealeased version.

## Versionning

Current release of SimuDraw is 1.0. 

It has been developed and tested on a Mac using a Python 2.7 interpreter but it should run normaly on any OS that has Python installed.




If you have any questions or suggestions please feel free to contact me. 

If you would like to contribute please fork this project.

