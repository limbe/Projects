#!/usr/bin/python
"""
Fibonacci Sequence;- Enter a number and have the program generate the
Fibonacci sequence to that number.
"""
numLimit = input(":>> ")
sequence = [0, 1]   #seed values
while sequence[-1] < numLimit:
     sequence.append(sequence[-1] + sequence[-1 -1])
del sequence[-1]
print sequence

