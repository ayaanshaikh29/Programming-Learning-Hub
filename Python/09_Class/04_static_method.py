#sometimes we need a function that doesn't use a self parameter at this case 
#we can define a static method like this

class Employee:
    language = "c++" #class attribute
    salary = 1200000 #class attribute

    @staticmethod #as it has no use of self parameter i.e. we used static method
    def greet(): 
        print("good Morning!!!")

    def getinfo(self): #self parametric function
        print(f"The name of employee is {self.name}. The language is {self.language}. The salary is {self.salary}")

employee1 = Employee()
employee1.name = "Ayaan" #instance attribute
employee1.language = "Python" #instance attribute

employee1.greet()
employee1.getinfo()
