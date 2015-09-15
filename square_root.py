# Going to make a program that guesses the square root of a number using Newton's Method 
# Hard Mode enables input recognition, and includes an iteration counter and lists guesses

user_num = input("Enter a positive number: ")

try:
    user_num = float(user_num)
    if user_num < 0:
        print("No negative numbers!")
    guess = user_num/2
    error = 1
    counter = 0
    while error > 0.01:
        x = (guess+(user_num/guess))*(1/2)
        error = guess - x
        counter += 1
        print("Current number of iterations: {}".format(counter))
        print("Current guess is: {}".format(guess))
        guess = x
    print("The square root of {} is {}.".format(user_num, guess))

except:
    print("Numbers only!") 

