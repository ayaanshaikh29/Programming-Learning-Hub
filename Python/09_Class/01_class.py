class Employee: #here Employee is a class
    language = "Python" #these two are class's attributes
    salary = 1200000

Employee1 = Employee() #here employee1 is object
Employee1.name = "Ayaan" #here name is objects attributes or instance's attribute
print(Employee1.name , Employee1.language , Employee1.salary)

Employee2 = Employee() #here employee2 is object
Employee2.name = "Azaan" #here name is objects attributes or instance's attribute
print(Employee2.name , Employee2.salary , Employee2.language)

#here name is objects attribute whereas language and salary 
#are class attribute as it belongs to class directly