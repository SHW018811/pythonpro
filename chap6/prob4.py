import random
guessarr = ["python","hangman","game"]
guessword = list(random.choice(guessarr))
chrarr = []
OX = False
emptyarr = ["_" for i in range(len(guessword))]

hangman = [["_______"],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|_______"]]
cnt = 0
while True:
    print("\n")
    chr = input("Enter your guess: ")
    chrarr.append(chr)
    print("\n")
    
    for i in range(len(guessword)):
        if(guessword[i] == chr):
            emptyarr[i] = chr
            OX = True
    if OX == True:
        print("Yes!",chr,"is in the word!")
        OX = False
    else :
        print("No!",chr,"is not in the word!")
        cnt+=1
    
    if cnt == 1:
        hangman[1]=["|    | "]
    elif cnt == 2:
        hangman[2]=["|    O "]
    elif cnt == 3:
        hangman[3]=["|    + "]
    elif cnt == 4:
        hangman[3]=["|   -+-"]
    elif cnt == 5:
        hangman[4]=["|    | "]
    elif cnt == 6:
        hangman[5]=["|   /| "]
    elif cnt == 7:
        hangman[6]=["|  / | "]
    for i in range(len(hangman)):
            print(hangman[i])
    if cnt == 7 :
        print("\nGame Over!")
        break
    
    print("\n\n")
    print("You've used the following letters:")
    print(chrarr)
    print("\n")
    print("Currently entered word: ")
    for i in range(len(emptyarr)):
        print(emptyarr[i],end=' ')
    print("\n\n")
    if(emptyarr == guessword):
        print("Success.")
        break


    
