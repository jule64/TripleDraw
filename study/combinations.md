**Here I am laying down some actual hands probabilities to test the accuracy
of the simulator.
Note for now I am only studying the probabilities of pre-flop events (i.e no drawing
or discarding of cards) to keep calculations manageable.**


## main probabilities

all-cards-combinations of 5 cards in a game of 52 cards:  
52 choose 5
// 2598960


Possible hands combinations using 5 cards:  

straight-flushes (5 consecutive cards of same suit):  
9*4
// 36

quads (4 same cards + one any):  
1 * 48 * 13
// 624

full-house (3 same cards + 1 pair):  
4 choose 3 * (4 choose 2 * 12) * 13
// 3744

flushes-ex-straight-flushes (5 non consecutive cards of same suit):  
13 choose 5 * 4 - (straight flushes)
// 5112

straights-ex-straight-flushes (5 consecutive cards not suited)):    
4^5*9-(straight flushes)
// 9180

trips-ex-full-house (3 same cards + 2 non pair cards):  
4 choose 3 * 4^2 * 12 choose 2 * 13
// 54912

two-pairs (2 pairs of different suits + one any):  
4 choose 2 * 4 choose 2 * 13 choose 2 * 44
// 123552

pocket-pairs (1 pair + 3 any non paired cards or trip cards):  
(4 choose 2 * 12 choose 3 * 4^3) * 13
// 1098240



## odds of hitting any hand pre flop:

all poss hands:  
(36+624+3744+5112+9180+54912+123552+1098240)=1295400

total combinations:  
2598960

Hit: 49.84%  
No hit: 1-0.4984=50.16%  



## Template for odds of hitting 'X' low:


total-allowed-cards:  
(allowed-ranks * 4) choose 5
// 658008


### hands probabilities in allowed cards:

excluded-ranks: 3  (A K Q for Jack low scenario)  
usable-card: 40 (Jack low scenario)  

straight-flushes (5 consecutive cards of same suit):  
(9 - excluded-ranks) * 4
//

quads (4 same cards + one any):
1 * (usable-card - 4) * (13 - excluded-ranks)
//

full-house (3 same cards + 1 pair):
4 choose 3 * (4 choose 2 * ((13 - excluded-ranks) - 1)) * (13 - excluded-ranks)
//

flushes-ex-straight-flushes (5 non consecutive cards of same suit):
(13 - excluded-ranks) choose 5 * 4 - (straight-flushes)
//

straights-ex-straight-flushes (5 consecutive cards not suited)):    
4^5 * (9 - excluded-ranks) - (straight-flushes)
//

trips-ex-full-house (3 same cards + 2 non pair cards):
4 choose 3 * 4^2 * ((13 - excluded-ranks) - 1) choose 2 * (13 - excluded-ranks)
//

two-pairs (2 pairs of different suits + one any):
4 choose 2 * 4 choose 2 * (13 - excluded-ranks) choose 2 * (usable-card - 8)
//

pocket-pairs (1 pair + 3 any non paired cards or trip cards):
(4 choose 2 * ((13 - excluded-ranks) - 1) choose 3 * 4^3) * (13 - excluded-ranks)
//

total-hittable-hands: sum of all the above


### odds of 'X' low

desired-cards = total-allowed-cards - total-hittable-hands

odds of Jack low = desired-cards / all-cards-combinations
