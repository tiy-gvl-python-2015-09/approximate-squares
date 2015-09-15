import math
from random import randint

def approx_sqrt(num):
    random_num = float(randint(1,num))
    previous_random_num = 0.0
    while float("{0:.3}".format(previous_random_num)) != float("{0:.3}".format(random_num)):
        previous_random_num = random_num
        error = (num - random_num**2)/2*random_num
        random_num = (1/2)*(random_num+(num/random_num))
    return random_num

print(approx_sqrt(int(input('What number do you want to square root? '))))
