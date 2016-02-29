excluded-ranks: 3 (A, K, Q)  
usable-card: 40


total-hittable-cards:  
((13 - 3)) * 4) choose 5
// 658008


straight-flushes (5 consecutive cards of same suit):  
(9 - 3) * 4
// 24

quads (4 same cards + one any):  
1 * (40 - 4) * (13 - 3)
// 360

full-house (3 same cards + 1 pair):  
4 choose 3 * (4 choose 2 * ((13 - 3) - 1)) * (13 - 3)
// 2160

flushes-ex-straight-flushes (5 non consecutive cards of same suit):  
(13 - 3) choose 5 * 4 - (straight-flushes)
// 984

straights-ex-straight-flushes (5 consecutive cards not suited)):  
4^5 * (9 - 3) - (straight-flushes)
// 6120

trips-ex-full-house (3 same cards + 2 non pair cards):  
4 choose 3 * 4^2 * ((13 - 3) - 1) choose 2 * (13 - 3)
// 23040

two-pairs (2 pairs of different suits + one any):  
4 choose 2 * 4 choose 2 * (13 - 3) choose 2 * (40 - 8)
// 51840

pocket-pairs (1 pair + 3 any non paired cards or trip cards):  
(4 choose 2 * ((13 - 3) - 1) choose 3 * 4^3) * (13 - 3)
// 322560


### odds of Jack low

desired-cards = 658008 - (24+360+2160+984+6120+23040+51840+322560) = 250920

odds of Jack low = 250920 / 2598960 = 0.09654631083
