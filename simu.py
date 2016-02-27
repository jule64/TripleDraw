
from strategy import Strategy
from deck import Deck



class SimuBuilder(object):

    def __init__(self):
        self.startingCards = ''
        self.numberDraws = 3
        self.target = 'J'
        self.simulations = 50000
        self._MAXCARDS = 5

    def setStartingCards(self, s):
        self.startingCards = s
        return self

    def setNumberOfDraws(self, d):
        self.numberDraws = d
        return self


    def setTarget(self, t):
        self.target = t
        return self


    def setSimulations(self, r):
        self.simulations = r
        return self

    def build(self):
        return Simu(self.startingCards, self.numberDraws, self.target, self.simulations,self._MAXCARDS)


class Simu(object):
    '''
    Responsible for running the simulations and
    assigning the compute load to the worker processes

    Use SimuBuilder to build this class safely
    '''

    def __init__(self,s,d,t,r,m):

        self.scards=s
        self.nDraws=d
        self.targ=t
        self.nSimu=r
        self._MAXCARDS=m



    def run(self):

        nbSuccess = 0
        #nber of simulations
        for u in range(self.nSimu):

            deck = Deck()

            #TODO hardcoded target change before release
            s1=Strategy(9)  # J LOW

            startingHand = self.getStartingHand(deck, self.scards)

            intHand=self.convertHandToIntegers(deck,startingHand)

            for v in range(self.nDraws):
                residualCards = s1.run(intHand)
                intHand=residualCards+self.convertHandToIntegers(deck,deck.retrieve(self._MAXCARDS-len(residualCards)))


            # at the end of the draws we check the hand one last time to see if we reached the target
            issuccess=s1.run(intHand,True)

            if issuccess:
                nbSuccess+=1

        return (nbSuccess+0.0)/self.nSimu



    def getStartingHand(self,deck, scards):

        #TODO rem after testing
        scards = []

        startingHand = []

        for i in range(5):
            startingHand.append(deck.getCard())

        return startingHand

    def convertHandToIntegers(self, deck, startingHand):

        return [deck.cardsToIntDict[j] for j in startingHand]





    