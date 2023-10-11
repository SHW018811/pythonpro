items = ["sword", "armor", "shield", "healing potion"]

print("Your items:")
for i in range(len(items)):
        print(items[i])

print("\nPress the enter key to continue.")
print("You have",len(items),"items in your possession.\n")

print("Press the enter key to continue.")
print("You will live to fight another day.\n")

num = int(input("Enter the index number for an item in inventory: "))
print("At index",num,"is",items[num],"\n")

sli1 = int(input("Enter the index number to begin a slice : "))
sli2 = int(input("Enter the index number to end the slice : "))
print("inventory[",sli1,":",sli2,"]\t\t",items[sli1:sli2],"\n")

print("Press the enter key to continue.")
print("You find a chest which contains:")
chest = ["gold","gems"]
print(chest)
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
items += chest
print(items)
print("\nPress the enter key to continue.")

print("\nYou trade your sword for a crossbow.")
print("Your inventroy is now:")
items[0] = "crossbow"
print(items)
print("\nPress the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
print("Your inventory is now:")
items[4:6] = ["orb of future telling"]
print(items)

print("\nPress the enter key to continue.")
print("In a great battle, your shield is destroyed.")
print("Your inventory is now:")
items.remove("shield")
print(items)

print("\nPress the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")
print("Your inventory is now:")
items.remove("crossbow")
items.remove("armor")
print(items)

print("\n\nPress the enter key to exit.")
