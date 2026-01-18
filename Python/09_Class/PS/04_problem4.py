class claculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The Square is :{self.n*self.n}")

    def cube(self):
        print(f"The cube is :{self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The Squareroot is :{self.n**0.5}")

    @staticmethod
    def greet():
        print("Hello User!!!")

c = claculator(100)
c.greet()
c.square()
c.cube()
c.squareroot()