import random

print("Welcom to Word Jumble!")
print("Unscramble the letters to make a word.")
words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
Jumble = random.choice(words)
mix = list(Jumble)
random.shuffle(mix)
print("Jumbled word: ",end='')
for i in range(len(mix)):
    print(mix[i],end='')
print()
guessword = input("Your guess: ")
if guessword == Jumble:
    print("Right, that's correct. The word was:",end='')
else :
    print("Sorry, that's not correct. The word was:",end='')

for i in range(len(Jumble)):
    print(Jumble[i],end='')
print()
