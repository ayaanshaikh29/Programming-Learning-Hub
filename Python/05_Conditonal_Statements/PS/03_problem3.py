s1 = "make alot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

message = input("Enter the comment: ")

if(s1.upper() in message.upper() or s2.upper() in message.upper() or s3.upper() in message.upper() or s4.upper() in message.upper()):
    print("It is a spam comment! BEAWARE!!!")

else:
    print("Your safe the comment is not spam.")