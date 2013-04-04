SimuDraw
========

An odds simulator for the game of 2-7 Triple Draw


Despite being one of the hottest games in online poker, little information can be found to improve your 2-7 Triple Draw skills.

SimuDraw tries to remedy to this problem by offering a virtual environment where users can simulate various games configurations and study their associated odds.

Before jumping in head first please carefully note that SimuDraw is a simulator, not a calculator, its results are hence an approximation of the actual odds and need to be taken as such.

To understand this difference, suppose you wanted to know the odds of being serve exactly a J low.  The actual odds are 4.9% and are given by the following formaula: C(9,4)*(5^4-4)/C(52,5)) = 4.9%.   Running this particular example twice with SimuDraw gave me a result of 4.87% and 4.95%, or approximately +/-0.1% around the actual value.


If you have any questions or suggestions please feel free to contact me. 

If you would like to contribute please fork this project.

Note: SimuDraw is a Python program and has been developed and tested using a Python 2.7 interpreter. As such I cannot garantee that it will work with earlier version Python or with Python 3.
