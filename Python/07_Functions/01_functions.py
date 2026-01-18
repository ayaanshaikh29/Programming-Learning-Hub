# function is a group of statement performiong a specific task
# when a program is dificult, bigger in size, and complex then fuction comes in use and makes it easier

'''
for example
a= int(input("enter a number:"))
b= int(input("enter a number:"))
c= int(input("enter a number:"))

average = (a+b+c)/2
print(average)
agar mujhe ye program 5 ya 10 ya 50 baar karna hota toh ye lengthy ho jata tab hum
function ka use karenge
'''
# Function Definition
def avg():
    a= int(input("enter a number: "))
    b= int(input("enter a number: "))
    c= int(input("enter a number: "))

    average = (a+b+c)/2
    print(average)

#isse ye function 5 baar run hoga 50 lines ka program in 10-11 lines
# Function Call
avg()
avg()
avg()
avg()
avg()