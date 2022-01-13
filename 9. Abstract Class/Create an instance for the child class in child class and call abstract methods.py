from abc import ABC, abstractmethod
class VehicleNoOfWheels(ABC):     ##abstarct class
    @abstractmethod   ##abstract method
    def __init__(Self):
        print("Bus having 6 wheels")

class Bus(VehicleNoOfWheels):
    def __init__(self):
        super(Bus, self).__init__()


b=Bus()
