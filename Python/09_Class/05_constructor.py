class Employee:
    language = "c++" #class attribute
    salary = 1200000 #class attribute

# __init__ is a type of dunder method.
# dunder method which is automatically called
    def __init__(self, name, language, salary):
        print("Good Morning!!")
        self.name = name
        self.language = language
        self.salary = salary

employee1 = Employee("Ayaan", "Python", 1500000) #when dunder methond is called 
#the class attributes are not valued
print(employee1.name , employee1.language , employee1.salary)