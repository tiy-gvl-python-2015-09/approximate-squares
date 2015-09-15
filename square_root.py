# Going to make a program that guesses the square root of a number using Newton's Method 


user_num = input("Enter a positive number: ")
guess = user_num / 2
error = 1

While error > 0.01:
    x = (guess + (user_num/guess))*(1/2)
    error = guess - x
    guess = x
print("The square root of {} is {}").format(user_num, guess)
    



