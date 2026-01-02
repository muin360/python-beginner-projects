import random

def check_guess(secret, guess):
    if guess == secret:
        print("Correct")
        return True
    elif guess < secret:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    return False


secret_number = random.randint(1, 10)
count = 0
max_attempts = 5

print("Guess the number between 1 and 10")
print("Max 5 attempt limit")

while True:
    user_guess = int(input("Enter your guess: "))
    count += 1

    if check_guess(secret_number, user_guess):
        print(f"You guessed it in {count} attempts")
        break

    if count == max_attempts:
        print("Game Over! You used all attempts 😢")
        print(f"The correct number was {secret_number}")
        break

    print(f"Attempts left: {max_attempts - count}")
