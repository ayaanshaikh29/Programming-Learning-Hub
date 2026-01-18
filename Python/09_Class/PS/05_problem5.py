from random import randint

class Train:
    def __init__(self,TrainNo):
        self.TrainNo = TrainNo

    @staticmethod
    def Greet():
        print("Namaskar Railway ticket online services mein aapka swagat hai!!")   

    def book(self, fro, to):
        print(f"Your Train is booked and  your train No is {self.TrainNo} which is travelling from {fro} to {to}.")

    def getstatus(self, fro, to):
        print(f"Your Train from {fro} to {to} is on time!!")

    def getFare(self,fro,to):
        print(f"Your Train No {self.TrainNo} from {fro} to {to} is costing you {randint(100,550)}.")  

T = Train(151083)
T.Greet()
T.book("Panvel" , "Pune")
T.getFare("Panvel" , "Pune")
T.getstatus("Panvel" , "Pune")

