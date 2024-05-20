import random
secret_number = random.randint(1, 10)
max_attempt = 3
def welcome_message():
    print("\nWelcome to number guessing game!")
    print(f"You have {max_attempt} attempts to guess the correct number.")
def guess_recursion(attempts_left):
    guess = int(input("\nGuess the number (between 1 nad 10):"))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
    else:
        print(f"Wrong guess. Attempts left: {attempts_left-1}")
        if attempts_left > 1:
           guess_recursion(attempts_left - 1)
        else:
            print(f"\nSorry, you couldn't guess the number. The correct number was {secret_number}.")
welcome_message()
guess_recursion(max_attempt)
print(f"Memory address of Secret Number {secret_number} is: {id(secret_number)}")