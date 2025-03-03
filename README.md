# Pattern factory and  SOLID

Typing must be applied in both tasks. INFO level logging should be used instead of the print statement. Use black to format the code.

## Task List:

**Task 1: Pattern factory**:

Implement a pattern factory that will allow you to create vehicles with different regional specifications without changing the main classes of vehicles.

- Create an abstract base class Vehicle with a start_engine() method.
- Change the Car and Motorcycle classes to inherit from Vehicle.
- Create an abstract class VehicleFactory with create_car() and create_motorcycle() methods.
- Implement two factory classes: USVehicleFactory and EUVehicleFactory. These factories should create cars and motorcycles with a region tag.
- Change the source code so that it uses factories to create vehicles.
