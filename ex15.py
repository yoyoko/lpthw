from sys import argv

script, filename = argv

txt = open(filename) #txt is now an object variable

print(f"Here's your file {filename}")
print(txt.read()) #performing a function on txt object
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
