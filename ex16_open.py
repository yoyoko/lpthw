from sys import argv

script, filename = argv

print("Now let's open it again")
target = open(filename)
print(target.read())
target.close()
