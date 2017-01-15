import random
secretNumber = random.randint(1, 100)
print("I'm thinking of a secret number between 1 and 100...")
while True:
    guess = int(input("What is your guess? "))
    if (guess == secretNumber):
        break
    if (guess > secretNumber):
        print("Sorry, your guess is too high.")
    if (guess < secretNumber):
        print("Sorry, your guess is too low.")
print("Dang, you got it!")