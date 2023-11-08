print("Creating a text file with the write() method.\n")
print("Reading the newly created file.")
text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("And that would make this the third line.\n")
text_file.close()
text_file = open("write_it.txt", "r")
for i in text_file:
    print(i,end='')
text_file.close()
print("\n")
print("Creating a text file with the writelines() method.\n")
print("Reading the newly created file.")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That make this line 3\n"]
text_file.writelines(lines)
text_file.close()

tf = open("write_it.txt", "r")
for i in tf:
    print(i,end='')

print("\n\n\nPress the enter key to exit.")
