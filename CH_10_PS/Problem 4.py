import random

class Train:
    def __init__(self, trainNO):
        self.trainNo = trainNO

    def book(self, fro, to):
        print(f"The train number {self.trainNo} is booked for go to {fro}{to}")
        
    def getStatus(self):
        print(f"The train number {self.trainNo} is on time ")
    
    def getFare(self,fro,to):
        print(f"The train number {self.trainNo} is go from {fro} to {to} is charge is {random.randint(3039-6000 )}RS. ")

t = Train(120990)
t.book("Mumbai" , "Delhi")  