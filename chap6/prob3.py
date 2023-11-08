geek = {"404":"clueless", "Unintalled" : "being fired."}

while True :
    print("\n\tGeek Translator\n")
    print("\t0 - Quit")
    print("\t1 - Look Up a Geek Term")
    print("\t2 - Add a Geek Term")
    print("\t3 - Redefine a Geek Term")
    print("\t4 - Delete a Geek Term")
    print("\t5 - Words in the dictionary\n")
    num = int(input("Choice : "))

    if num == 0 :
        break
    elif num == 1 :
<<<<<<< Updated upstream
        find = input("What term  do you want me to translate?: ")
        if find in geek:
            print(find,"means",geek[find])
        else:
            print("I have no idea what",find,"is.")
=======
        
>>>>>>> Stashed changes
    elif num == 2 :
        add = input("Enter characters to add: ")
        if add in geek:
            print("Already exists")
        else :
            means = input("Enter the meaning of the characters: ")
            geek[add] = means
    elif num == 3 :
        reply = input("Enter the character you want to redefine: ")
        if reply in geek:
            remeans = input("Meaning of character to override: ")
            geek[reply] = remeans
        else :
            print("It does not exist.\n")
    elif num == 4 :
        delchr = input("Enter the word you want to delete: ")
        if delchr in geek:
            print("Deleted successfully.")
            del geek[delchr]
        else :
            print("That word doesn't exist")
    elif num == 5 :
        print("\nWords registered in the dictionary>> ",end='')
        for key, value in geek.items():
            print("[",key,"]", end = ' ')
        print("\n")
