###  Part E: Real-World If-Else + Loops (10 tasks)
# 49. Simulate a guessing game (user guesses a number until correct).




import random

secret_number = random.randint(1, 100)

print(" Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


attempts = 0
guess=-1

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")
        
    else:
        print(f"Congratulations! You guessed it right in {attempts} attempts.")
