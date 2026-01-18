f = open("file.txt") # This will open the file
print(f.read()) # This will print the content in the file
f.close() # To close the file we use this

# We can open as well as close this more easily by using with statement
with open("file.txt") as f:
    print(f.read())

# You don't have to explicitly close the file