import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter a number greater than zero")
    else:
        print("Enter any number.")

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses +=1
        user_guess = input("Guess:")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Enter a number:")

        if user_guess == random_number:
            print("You got it!")
        elif user_guess > random_number:
            print("You were above the number.")
        else:
            print("You were below the number!")
print("You got it in", guesses, "guesses")
