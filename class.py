class Car(object):
    def __init__(self, model, color, company, topspeed):
        self.model = model
        self.color = color
        self.company = company
        self.topspeed = topspeed

    def start(self):
            print("Started")

    def stop(self):
            print("Stopped")

    def accelerate(self):
            print("Accelerating")

    def changeGear(self):
            print("Gear Changed")
            

audi = Car("A6","Red","Audi","210 Km/ph")
print(audi.start())
print(audi.stop())
print(audi.accelerate())
print(audi.changeGear())