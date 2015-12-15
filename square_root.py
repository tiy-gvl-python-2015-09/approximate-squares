describe "square_root.py: returns the approximate square root of a positive number"


# Got it!

number = 600
print(number)
previous_number = number / 2

while previous_number - previous_number_two > abs(.01):
    previous_number = (previous_number + number/previous_number) / 2
    previous_number_two = (previous_number + number/previous_number) / 2
    print(previous_number_two)
print (' ')

number = random.randint(1,5000)
print(number)
previous_number = number / 2

while previous_number - previous_number_two > abs(.01):
    previous_number = (previous_number + number/previous_number) / 2
    previous_number_two = (previous_number + number/previous_number) / 2
    print(previous_number_two)

def product(x,y):
    return x * y
