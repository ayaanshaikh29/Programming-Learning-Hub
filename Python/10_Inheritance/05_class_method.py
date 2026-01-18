'''
class method is a method which is bounded with class not with the object
'''
class Employee:
    a = 1 #class attribute
    #to bind with only class but not with the object we use class method
    @classmethod
    def show(cls):
        print(f"The class attribute value of a is: {cls.a}")

e = Employee()
e.a = 7 #instance attribute (using object)
e.show()
# after using classmethod we can see that the output is class attribute's value but not
# the instance's attribute value