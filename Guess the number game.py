import random

def guess_the_number():
    score = 0
    print("Welcome to guess the Number g@me! ")
    print("Guess a number beteen 1 and 10. Lets begin!\n")

    while True:
        number_to_guess = random.randint(1,10)
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess (1-10): "))
                attempts = attempts + 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high. Try again!")
                else:
                    print(f"Correct! you guessed it in {attempts} attempts.")
                    score = score + 1
                    print(f"Your current score: {score}\n")
                    break
            except ValueError:
                print("Please enter a valid number between 1 and 10.")
guess_the_number()
