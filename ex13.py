from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

name = input("What's your name ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third varibale is:", third)
print(f"Your name is {name}")
