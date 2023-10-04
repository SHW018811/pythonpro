import random

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
rword = random.choice(words)
cnt = len(rword)

print(guessword)

#print("Length of the selected word:",cnt)
#while True:
#   if cnt == 0 : break
#   print("Remaining attemps:",cnt)
#   print("Current guessed word:",guessword)
    
