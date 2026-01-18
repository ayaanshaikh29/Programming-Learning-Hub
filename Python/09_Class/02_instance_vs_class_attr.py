class Employee:
    language = "python" #class attribute
    salary = 1200000 #class attribute

employee1 = Employee()
employee1.name = "Ayaan" #instance attribute
employee1.language = "c++" #instance attribute
print(employee1.name , employee1.language , employee1.salary)

#after getting output it is observed that the class attribute is overpowered by the 
#instance attribute