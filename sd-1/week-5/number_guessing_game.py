import random
number=random.randint(1,100)

guess=None
guessCounter=0
while guess != number:
    guess = int(input("Guess a number between 1 and 100:"))
    guessCounter +=1
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low!")

print(f"Congratulations the guess was correct! It took {guessCounter} guesses")
