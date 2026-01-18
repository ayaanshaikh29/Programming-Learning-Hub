class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def Bark():
        print("Bhow Bhow!!!")
    
d = Dog()
d.Bark()