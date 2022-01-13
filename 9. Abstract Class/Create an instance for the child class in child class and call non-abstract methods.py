from abc import ABC, abstractmethod
class VehicleNoOfWheels(ABC):     ##abstarct class
    @abstractmethod   ##abstract method
    def __init__(Self):
        pass

class Car():
    def __wheels__(self):
        print("Car having 4 wheels")
        


b=Car()
b.__wheels__()
