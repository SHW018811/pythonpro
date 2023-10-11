list = {}
name = []
while True:
    print("\tHigh Scores Keeper")
    print("\n\t0 - Quit")
    print("\t1 - List Scores")
    print("\t2 - Add a Score")
    print("\n")
    num = int(input("Choice: "))
    if num == 0 :
        break
    elif num == 1 :
        print("\nHigh Scores\n")
        print("NAME\tSCORE")
        for i in range(len(name)):
            print(name[i],"\t",list.get(name[i]))
        print("\n")
    elif num == 2 :
        print("\n")
        addname = input("What is the player's name?: ")
        name.append(addname)
        addscore = input("What score did the player get? : ")
        list[addname] = addscore
