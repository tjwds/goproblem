# goproblem.py (3.5.1)
# dumb dumb dumb

import random

rows = 3
columns = 5

number = rows * columns
boop = []
pieces = ["⚪", "⚫", "+"]

for x in range(number):
    coolint = random.randint(0,2)
    boop += pieces[coolint]

for y in range(rows-1, 0, -1):
    boop.insert(((y*columns)), "\n")

boopbeep = ''.join(boop)
print(boopbeep)
    
