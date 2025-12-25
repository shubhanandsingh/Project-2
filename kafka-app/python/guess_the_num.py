import random
secretNumber = random.randint(1, 20)
#///////guess the number
print("type the guessed number, the game will have six rounds")
for guessTaken in range(1,7):
    print("take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("your guess is too low")
    elif guess > secretNumber:
        print(" your guess is too high")
    else:
        break
if guess == secretNumber:
    print("good job, you guessed my number in " + str(guessTaken) + "guesses")
else:
    print("nope, the number i was thinking was " + str(secretNumber))