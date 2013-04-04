SimuDraw
========

An odds simulator for the games of 2-7 Triple &amp; Single Draw


2-7 Triple &amp; Single Draw are the hottest games in online poker right now.  As with any poker games, a strong understanding of the odds is critical to become a successful player.

SimuDraw helps you simulate various game configurations/hands and quickly generate the associated odds, such as the odds of hitting an 8 low or a 9 low.

SimuDraw works by simulating thousands of draws per simulation and then averaging the results to approximate the actual odds.  As such you will find that the odds it generates are always slightly different from those that one would obtain using traditional probabilistic formulas.  The current calibration ensure those difference are small however.
For example, the odds of drawing a J low exactly are 4.9% (= C(9,4)*(5^4-4)/C(52,5)).  SimuDraw gives between 4.87% and 4.95%


Note that SimuDraw is a Python program and has been tested on Python 2.7. Other version of Python can possibly be used although they have not been tested.

If you would like to contribute please fork this project.  If you have any questions please feel free to send me an email.
