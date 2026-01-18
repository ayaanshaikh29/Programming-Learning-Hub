'''
Inheritance is a way of creating a new class from an existing class
'''
class employee: #Base class
    company = "Infotech"
    def show(self):
        print(f"The name of the employee is {self.name} and his salary is {self.salary}")

#METHOD 1
class programmer:
    company = "Amazon"
    #we have to write the function of previous class again in new class which can be a lengthy
    #method and error prone too
    def show(self):
        print(f"The name of the employee is {self.name} and his salary is {self.salary}")

    def showlanguage(self):
      print(f"The name of the employee is {self.name} and his language is {self.langauge}") 
       
#METHOD 2
class programmer(employee):#Derived class
    company = "Amazon"
    def showlanguage(self):
      print(f"The name of the employee is {self.name} and his language is {self.langauge}") 

a = employee()
b = programmer()
a.name = "Ayaan"
a.salary = 1200000
b.name = "Azaan"
b.salary = 1500000
b.language = "python"
print(a.company, a.name, a.salary)
print(b.company, b.name, b.salary, b.language)
#the output will be same 