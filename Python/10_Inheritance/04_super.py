'''
SYNTAX :- "super().__init__()"
'''

class Employee: # Parent Node
    def __init__(self): #this function will call by itself
        print("Constructor of Employee.")
    a = 1

class Programmer(Employee): # Children1 Node
    def __init__(self): #this function will call by itself
        super().__init__() #this will help in printing the parent class function too for eg 
        #in this case it will print class programmer but it will also print its parent
        print("Constructor of Programmer.")
    b = 2 

class Manager(Programmer): # Children2 Node
    def __init__(self): #this function will call by itself
        super().__init__() #it helps in calling parent class that is programmer and employee
        print("Constructor of Manager.")
    c = 3

o = Employee()
print(o.a)

o = Programmer()
print(o.a,o.b) 

o = Manager()
print(o.a,o.b,o.c)