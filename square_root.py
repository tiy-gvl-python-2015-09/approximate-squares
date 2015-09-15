def better_approximate_square_root():
    user_input = input("Enter a positive number: ") # Prompts the user for a number
    user_input_no_dec = user_input.replace(".", "") # Removes the decimal if not a whole number
    user_input_no_neg = user_input_no_dec.replace("-", "") # Removes the minus if negative number

    if user_input_no_neg.isdigit() == False: # Checks user input to make sure they put in a number
        print("That's not a number. Please try again.")
        better_approximate_square_root()
    elif float(user_input) < 0:
        print("That's a negative number. Please try again.")
        better_approximate_square_root()
    else:
        user_number = float(user_input)
        guess = user_number/2
        count = 1
    
        while abs((user_number - (guess**2))) > 0.01:
            print("Square root guess number {}: {}".format(count, guess))
            new_guess = (guess + (user_number/guess))/2
            guess = new_guess
            count += 1
        
        print("The square root of {} is {}".format(user_number, guess))
        

better_approximate_square_root()
