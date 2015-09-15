import math
from random import randint

def approx_sqrt(num):
    guess = float(randint(1,num))
    previous_guess = 0.0
    while float("{0:.3}".format(previous_guess)) != float("{0:.3}".format(guess)):
        previous_guess, guess = guess, (1/2)*(guess+(num/guess))
    return guess

print(approx_sqrt(int(input('What number do you want to square root? '))))
