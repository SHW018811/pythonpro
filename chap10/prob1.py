print("Opening and closing the file.\n")
print("Reading characters from the file.")
text_file = open("read_it.txt", "r")

print(text_file.read(1))
print(text_file.read(5),"\n")
text_file.close()

text_file = open("read_it.txt", "r")
print("Reading the entire file at once.")
whole_thing = text_file.read()
print(whole_thing,"\n")
text_file.close()

text_file = open("read_it.txt", "r")
print("Reading characters from a line.")
print(text_file.readline(1))
print(text_file.readline(5),"\n")
text_file.close()

text_file = open("read_it.txt", "r")
print("Reading one line at a time.")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline(), "\n")
text_file.close()

text_file = open("read_it.txt", "r")
print("Reading the entire file into a list.")
lines = text_file.readlines()
print(lines,"\n")
num = int(input())
text_file.close()
text_file = open("read_it.txt","r")
for i in range(num):
   print(text_file.readline())
print()
text_file.close()

text_file = open("read_it.txt", "r")
print("Looping through the file, line by line.")

for line in text_file:
    print(line)

text_file.close()
