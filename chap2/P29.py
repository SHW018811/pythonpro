name = input("What's your name? ")
age = int(input("And how old are you? "))
weigh = int(input("Okay, last question. How many pounds do you weigh? "))

save = age/7
save2 = age * 31536000

print("Did you know that you're just",save,"in dog years?")
print("\nBut you're also over",save2,"seconds old.")

print("\nIf a small child were trying to get your attention, your name would become ",name,name,name,name,name,sep="")
moon = weigh / 6
sun = weigh * 27.1
print("\nDid you know that on the moon you would weigh only",moon,"pounds?")
print("But on the sun, you'd weigh",sun,"<but, ah... not for long>.")
print("\nPress the enter key to exit.")
