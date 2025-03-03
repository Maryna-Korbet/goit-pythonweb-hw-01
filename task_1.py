#Implement the Factory pattern to create vehicles with different regional 
#specifications without modifying the core vehicle classes.

import logging
from abc import ABC, abstractmethod
from typing import Type


# Login settings
logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ]
)

# Abstract vehicle class
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass

class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): The engine is running")

class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): The motor is started")

# Abstract factory class
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Type[Car]:
        pass
    
    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Type[Motorcycle]:
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
         return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")
    
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


# Test
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Test US
us_car = us_factory.create_car("Toyota", "Corolla")
us_car.start_engine()
logging.info('The USA car has been successfully created and is ready to use')

us_motorcycle= us_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_engine()
logging.info('The USA motorcycle has been successfully built and is ready for use')

# Test EU
eu_car = eu_factory.create_car("Volkswagen", "Golf")
eu_car.start_engine()
logging.info('The EU car has been successfully created and is ready to use')

eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Panigale V4")
eu_motorcycle.start_engine()
logging.info('The EU motorcycle has been successfully built and is ready for use')

