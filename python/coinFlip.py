#!/usr/bin/python
"""
from rosetta.org
author: donibrysonimbaga
program: coinFlip.py

Write some code that simulates flipping a single coin however many 
times the user decides. The code should record the outcomes and count 
the number of tails and heads
"""

import random
n = input("For how many? ")
sides = ["tail", "head"]
h, t = 0, 0
for n in xrange(n):
     coin = random.choice(sides)
     print coin
     if coin == "tail":
          t += 1
     elif coin == "head":
          h += 1

print ""
print "head =",h,"\n","tail =",t
