import random
from time import sleep as delay
import os

def generate_binary_number(length):
    binary = ""
    for _ in range(length):
        bit = random.choice(["0", "1"])
        binary += bit
    return binary

def get_guess_from_user(length):
    while True:
        guess = input(f"Enter your guess ({length} digits binary number): ")
        if len(guess) != length or not guess.isdigit() or any(char != "0" and char != "1" for char in guess):
            print(f"Invalid guess. Please enter a {length}-digit binary number.")
        else:
            return guess

def compare_binary_numbers(target, guess):
    if target == guess:
        return "Congratulations! You guessed the correct number."
    else:
        match_count = sum(1 for i in range(len(target)) if target[i] == guess[i])
        return f"Incorrect. {match_count} out of {len(target)} digits match."

def play_game():
    difficulty = input('Enter difficulty with 0 to 5 stars (e.g. *****): ')
    length = len(difficulty)
    target = generate_binary_number(length)
    attempts = 0

    print("Welcome to 'Guess the Binary Number'!")
    print('The rules are: guess a binary number, and check your answer.')
    print(f"A random {length}-digit binary number has been generated.")
    print("Try to guess the number in")
    delay(3)
    for sec in range(3):
        os.system('cls')
        print(3 - sec)
        delay(1.5)
    os.system('cls')
    print()
    while True:
        guess = get_guess_from_user(length)
        attempts += 1

        result = compare_binary_numbers(target, guess)
        print(result)

        if target == guess:
            break

    print("You guessed the number in {} attempts.".format(attempts))

# Start the game
play_game()
