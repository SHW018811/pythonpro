print("Input your string...")
fp = open("write_it.txt", "w")
while True:
    sttr = input(">> ")
    if sttr == "Q": break
    fp.write(sttr)
    fp.write("\n")

print("Write process has been finished")

print("\n\n\nYour inputs are below..")
fp.close()
fp = open("write_it.txt", "r")
for pr in fp:
    print(pr,end='')

