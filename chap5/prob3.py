import random

a = False
b = False
print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
rword = random.choice(words)
cnt = len(rword)
guessword = ["_" for i in range(cnt)]
print(guessword)
print("Length of the selected word:",cnt)
print(rword)
while True:
   if cnt == 0 : break
   print("Remaining attemps:",cnt)
   print("Current guessed word: ",end = '')
   for i in range(len(rword)):
       print(guessword[i],end=' ')
   print()
   inguess = input("Guess a letter: ")

   #right -> change
   for i in range(len(rword)):
       if(inguess == rword[i]):
           guessword[i] = inguess
           a = True
   if a != True:
       cnt -= 1
   a = False
    
   if "_" in guessword:
        continue
   else :
      b = True
      print("Congratulations! You guessed the word:",rword)
      break
if b == False : print("Incorrect guess.\nYou've used up all your attempts. The correct ord was python.")
#no -> cnt -- kee   
