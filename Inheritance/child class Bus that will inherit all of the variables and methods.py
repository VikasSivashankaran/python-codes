class Vechicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vechicle):
    pass

school_bus=Bus("Scania", 200, 12)
print("Vehicle name is ",school_bus.name,"and Speed of the bus is ",school_bus.max_speed," Scania's milege is",school_bus.mileage)
