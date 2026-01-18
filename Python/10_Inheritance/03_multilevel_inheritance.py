class Employee: # Parent Node
    a = 1

class Programmer(Employee): # Children1 Node
    b = 2 

class Manager(Programmer): # Children2 Node
    c = 3

o = Employee()
print(o.a) # print the value of a as there is an attribute present is employee

o = Programmer()
print(o.a,o.b) # print the value of a,b as there is an attribute present is programmer(b)
# but programmer consist class employee(a) so a will also get print

o = Manager()
print(o.a,o.b,o.c) # print the value of a,b,c as there is an attribute present is Manager(c)
# but Manager consist of class programmer which again consist a class of employee so it will
# it will also print the value a,b,c