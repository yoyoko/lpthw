from sys import argv

script, input_file = argv

#prints the whole file "f"
def print_all(f):
    print(f.read())

#resets the file to the beginning
def rewind(f):
    f.seek(0)

#sets up line counter and line
def print_a_line(line_count, f):
    print(line_count, f.readline())

#creates an object variable. Input_file = argv
current_file = open(input_file)

print("First let's print the whole file:\n")
 #prints all of the argv input
print_all(current_file)

#rewind the argv input
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

current_file.close()
