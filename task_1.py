#Implement the Factory pattern to create vehicles with different regional 
#specifications without modifying the core vehicle classes.

from abc import ABC, abstractmethod


# Abstract vehicle class
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): The engine is running")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): The motor is started")

# Abstract factory class
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass
    
    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
         return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


# Test
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Test US
us_car = us_factory.create_car("Toyota", "Corolla")
us_car.start_engine()

us_motorcycle= us_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_engine()

# Test EU
eu_car = eu_factory.create_car("Volkswagen", "Golf")
eu_car.start_engine()

eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Panigale V4")
eu_motorcycle.start_engine()
