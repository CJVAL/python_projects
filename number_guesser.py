from curses.ascii import isdigit
import random

maximum_value = input("Enter any number (More than 0) ")
guesses = 0
if maximum_value.isdigit():
    maximum_value = int(maximum_value)

    if maximum_value <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number next time")
    quit()


random_number = random.randint(0, maximum_value)

while True:
    guesses += 1
    user_guess = input("Guess a number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Error! \nPlease enter a number next time! ")
        continue
    
    if user_guess == random_number:
        print("Congrats you guessed the correct number!")
        print(f"You got the correct answer in {guesses} guesses!")
        break
    else:
        if user_guess > random_number:
            print("Guess is too high")
        elif user_guess < random_number:
            print("Guess is too low")