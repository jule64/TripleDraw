SimuDraw
========

An odds simulator for the game of 2-7 Triple Draw


Despite being one of the hottest game in online poker currently, there is little information out there to help one improve his 2-7 Triple Draw skills.

SimuDraw tries to remedy to this problem by offering a virtual environment where users can simulate various games configurations and study the associated odds.

SimuDraw generate its results by simulating a large amount of draws and averaging the results.  As such please carefully note that it does not provide exact odds but approximations of the actual odds.

To help understand the difference, suppose you wanted to know what are the chances of being served exactly a J low from the start.  The odds of this event happening are 4.905% and are given by the following formula: C(9,4)*(5^4-4)/C(52,5)) = 4.9%. Using SimuDraw gave a result of 4.87% the first time and 4.95% the second or +/-0.1% from the actual value.


If you have any questions or suggestions please feel free to contact me. 

If you would like to contribute please fork this project.

Note: SimuDraw is a Python program and has been developed and tested using a Python 2.7 interpreter. As such I cannot garantee that it will work with earlier version Python or with Python 3.
