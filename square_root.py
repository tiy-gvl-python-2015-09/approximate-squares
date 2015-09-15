# Going to make a program that guesses the square root of a number using Newton's Method 


user_num = input("Enter a positive number: ")

if user_num < 0:
    print("No negative numbers!")

user_num = float(user_num)
guess = user_num / 2
error = 1
counter = 0
iteration_list = []
guess_list = []

While error > 0.01:
    x = (guess + (user_num/guess))*(1/2)
    error = guess - x
    guess_list.append(guess)
    counter += 1
    iteration_list.append(counter)
    print("Current number of iterations: {}".format(len(iteration_list)))
    print("Current guess is: {}".format(guess))
    guess = x
print("The square root of {} is {}").format(user_num, guess)
    



