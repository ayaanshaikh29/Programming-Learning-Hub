class Employee:
    a = 1 #class attribute

    @classmethod
    def show(cls):
        print(f"The class attribute value of a is: {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 7 #instance attribute (using object)
e.name = "Ayaan Shaikh"

#type 1
print(e.name) #prints whole name
#type 2
print(e.fname) #prints first name
print(e.lname) #prints last name
#type 3
print(e.fname,e.lname) #prints first and last name together

e.show()