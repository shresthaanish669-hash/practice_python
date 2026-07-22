class Toyota:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "car has started.")

    def stop(self):
        print(self.brand, "car has stopped.")

class Fortuner(Toyota):
    def __init__(self, brand, model):
        super().__init__(brand) #it iherits the parent constructor value (Super keyword) 
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car = Fortuner("Toyota", "Fortuner")

car.display()
car.start()
car.stop()