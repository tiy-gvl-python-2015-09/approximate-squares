from random import random
from random import randint

square = float(input())
potential_sqrt = randint(0,int(square)) + random()

while potential_sqrt **2 > square + 0.001:
    potential_sqrt -= 0.001
    continue

while potential_sqrt **2 < square - 0.001:
    potential_sqrt += 0.001
    continue

print(potential_sqrt)
