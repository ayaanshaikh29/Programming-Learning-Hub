username = input("Enter your username: ")

if(len(username)<10):
    print("Your username has less than 10 characters")

else:
    print("username not accepted (your username contains more than  or equal to 10 characters)")