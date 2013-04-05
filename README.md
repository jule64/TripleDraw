SimuDraw
========

SimuDraw is an odds simulator for the game of 2-7 Triple Draw


## Background Info

Despite being one of the hottest games in online poker, there is little information out there to help one improve his 2-7 Triple Draw skills.

SimuDraw tries to remedy this problem by offering a virtual environment for users to study the outcomes of various hands and game configurations and their associated odds.


## How it works

SimuDraw produces its results by generating a large amount of draws and averaging the results of those draws.  As such please carefully note that SimuDraw does not provide exact odds but instead approximations of the actual odds.

To help understand the difference, suppose you wanted to know what the chances are of being dealt a J low pre-flop.  The odds of this event are 4.905% and are given by the following formula: C(9,4)*(5^4-4)/C(52,5)) = 4.9%. By contrast SimuDraw gave a result of 4.87% on the first run of simulation and 4.95% on the second, or roughly +/-0.1% away from the actual value.


## Versionning

Current release of SimuDraw is 1.0. 

It has been developed and tested on a Mac using a Python 2.7 interpreter but it should run normaly on any OS that has Python installed.




If you have any questions or suggestions please feel free to contact me. 

If you would like to contribute please fork this project.

