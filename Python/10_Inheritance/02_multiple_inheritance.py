class employee: #parent class 1
    name = "Azaan"
    company = "Infotech"
    def show(self):
        print(f"The name of the employee is {self.name} and his company is {self.company}.")

class coder: #parent class 2
    language = "Python"
    def printlanguage(self):
        print(f"The langauge you are good at is {self.language}.")

class programmer(employee,coder): #child class
    company = "Amazon"
    salary = 1500000
    def showlanguage(self):
      print(f"The name of the employee is {self.name}, his salary is {self.salary}.") 

b = programmer()
b.show()
b.showlanguage()
b.printlanguage()

