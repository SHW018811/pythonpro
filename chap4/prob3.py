import random
print("\t\tWelcome to 'Guess My Number'!")

print("I'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as possible.\n")

Think = random.randrange(1,101)
trynum = 0
print(Think)
while True:
    guessnum = int(input("Take a guess: "))
    trynum += 1
    if guessnum > Think : print("Lower...")
    elif guessnum < Think : print("Higher...")
    elif guessnum == Think :
        print("You guessed it!  The number was", Think)
        print("And it only took you",trynum,"tries!")
        break
print("\n\n\nPress the enter key to quit.")
