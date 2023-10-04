item = ("sword", "armor", "shield", "healing potion")
print("Your items:")
for inv in item:
    print(inv)

print("\nPress the enter key to contine.")
print("You have",len(item),"items in your possession.")
print("\nPress the enter key to continue.")

if "healing potion" in item:
    print("You will live to figh another day.")

sel = int(input("Enter the index number for an item in inventory:"))
print("At index",sel,"is",item[sel],"\n")

sli1 = int(input("Enter the index number to begin a slice: "))
sli2 = int(input("Enter the index number to end the slice: "))
print("inventory[",sli1,":",sli2,"]","\t\t",item[sli1:sli2])
print("\nPress the enter key to continue.")
print("You find a chest. It contaions:")
chest = ("gold", "gems")
print(chest)
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
item += chest
print(item)
print("\n\nPress the enter key to exit")
