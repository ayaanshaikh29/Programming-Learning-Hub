class Employee:
    language = "c++" #class attribute
    salary = 1200000 #class attribute

    def greet(self): #self parametric function
        print("good Morning!!!")

    def getinfo(self): #self parametric function
        print(f"The name of employee is {self.name}. The language is {self.language}. The salary is {self.salary}")

employee1 = Employee()
employee1.name = "Ayaan" #instance attribute
employee1.language = "Python" #instance attribute

# Method 1
employee1.greet()
employee1.getinfo()

# Method 2
Employee.greet(employee1)
Employee.getinfo(employee1)