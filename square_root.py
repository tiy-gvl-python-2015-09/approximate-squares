from random import randint
from math import ceil

def approximate_square_root():
    user_number = float(input("Enter a positive number: "))
    guess = float(randint(0, ceil(user_number)))
    
    while abs((user_number - (guess**2))) > 0.01:
        new_guess = (guess + (user_number/guess))/2
        guess = new_guess
    print("The square root of {} is {}".format(user_number, guess))

approximate_square_root()


def better_approximate_square_root():
    user_number = float(input("Enter a positive number: "))
    guess = user_number/2
    count = 1
    
    while abs((user_number - (guess**2))) > 0.01:
        print("Square root guess number {}: {}".format(count, guess))
        new_guess = (guess + (user_number/guess))/2
        guess = new_guess
        count += 1
        
    print("The square root of {} is {}".format(user_number, guess))

better_approximate_square_root()
