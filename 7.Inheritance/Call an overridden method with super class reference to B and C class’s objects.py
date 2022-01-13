class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")


class BMW(Car):

    def __init__(self):
        super().__init__()
        print("You just created the BMW instance")

    def drive(self):
        super().drive()
        print("You are driving a BMW, Enjoy...")

    def headsup_display(self):
        print("This is a unique feature")


class BMW320(BMW):

    def __init__(self):
        super().__init__()
        print("You created BMW320 instance")

    def drive(self):
        super().drive()
        print("You are enjoying BMW 320")

    def speed(self):
        print("Maximum car speed is 260km/h")


c = Car()
c.drive()
c.stop()
b = BMW()
b.drive()
b.stop()
b.headsup_display()
b320 = BMW320()
b320.drive()
b320.speed()
