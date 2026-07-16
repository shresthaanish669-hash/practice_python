class Car:
    def __init__(self):
        self.accelator = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelator = True
        print("car started..")

car1 = Car()
car1.start()
