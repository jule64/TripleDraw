SimuDraw
========

SimuDraw is an odds simulator for the game of 2-7 Triple Draw


## Background Info

Despite being one of the hottest games in online poker, 2-7 Triple Draw lacks badly of online resources and free tools to help players improve their game.

SimuDraw tries to fill this gap by providing players a virtual environment for studying various hands/game configurations and their associated odds.


## How it works

SimuDraw produces drawing statistics by simulating a large amount of draws and averaging their results.  As such please note that SimuDraw does not provide exact odds but instead approximations of the actual odds.

To illustrate the difference, suppose you wanted to know the chances of being dealt a J low pre-flop.  The odds of this event are 4.905% (C(9,4)*(5^4-4)/C(52,5)) = 4.9%). SimuDraw, by comparison gave a result of 4.87% and 4.95% in two separate runs (using 50,000 simulations per run). This gives a precision of roughly 0.1% away from the actual value.  That difference becomes less than 0.01% with 200k simulations per run.


## Performances

The current version of SimuDraw (1.0) has an average processing time of 7 seconds per 50,000 simulations, down from 13 seconds for the initial unreleased version.

## Versionning

Current release of SimuDraw is 1.0. 

SimuDraw has been developed and tested on a Mac OSX using a Python 2.7 interpreter. It should however run normaly on any platform that has Python installed.



If you have any questions or suggestions please feel free to contact me. 

If you would like to contribute please fork this project.

