#Program to guess a number by a user.

# Algorithm
# Start the program with a constant while loop
# Ask user to guess a number.
# if correct, say correct and terminate
# Else, ask question 



prompt = "\nGuess the number: "

active = True
random_num = 5
while active:
    user_guess = int(input(prompt))

    if user_guess == random_num:
        print("Your guess is right")
        active = False   
    else:
        if user_guess > random_num:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    
