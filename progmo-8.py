'''
 Write a program to create a number guessing game for the user. The program should ask the user to input a number. The program specifications are as mentioned below.
I.	The program should generate a random number for the answer.[2.5]
II.	The program should prompt the user for a number input.[2.5]
III.	The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).[2.5]
IV.	The program should check the user input for 5 times and allow the users to guess for at most 5 times if their input don't match the answer number.[2.5]
V.	If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit. [5]


'''

import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I've selected a number between 1 and 100.")
print("You have 5 attempts to guess the correct number.")

# Counter for the number of guesses
attempts = 0
max_attempts = 5

# Game loop
while (attempts < max_attempts):
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # Increment the attempt counter
    attempts += 1
    
    # Check the guess and provide feedback
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print(f"Correct number! You guessed it in {attempts} attempts.")
        break
    
    # Check if the player has used all attempts
    if attempts == max_attempts and guess != answer:
        print(f"Game Over! You've used all {max_attempts} attempts.")
        print(f"The correct number was {answer}.")

print("Thank you for playing!")