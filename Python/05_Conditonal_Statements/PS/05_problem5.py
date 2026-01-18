names = ["ayaan".upper(), "azaan".upper(), "armaan".upper(), "hasan".upper(), "ajaaz".upper(), "faateh".upper(), "manav".upper()]

n = input("Enter a name: ")

#to use both lower and upper case use .lower() and .upper()
if(n.upper() in names):
    print("the name is peresnt in the list!")

else:
    print("name not found!")