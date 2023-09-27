import random
print("I sense your energy. Your true emotions are coming across my screen")
print("You are...")
face = random.randrange(0,3)

print("__________")
print("|         |")
print("| O     O |")
print("|   <     |")
print("|         |")

if face == 0:
    print("|    \\/   |")
elif face == 1:
    print("|    /\\   |")
elif face == 2:
    print("|   ___   |")

print("|_________|\n")
print("...today.")
print("\n\nPress the enter key to quit.")
