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

*Setup and Usage*:
1. Clone the repository:
git clone https://github.com/Maryna-Korbet/goit-pythonweb-hw-01.git
2. Install required dependencies:
No external dependencies are required, as the code uses Python's built-in libraries (e.g., logging).
3. Run the code:
You can run the script directly from the command line:
python task_1.py

**Task 2: SOLID**:

This is a simplified library management program that demonstrates the principles of SOLID design. The system allows users to add, remove, and show books in a library. The code follows SOLID principles to ensure maintainability, scalability, and extensibility.

- Single Responsibility Principle (SRP): The Book class is responsible for storing information about books, while the Library class is responsible for managing books.
- Open/Closed Principle (OCP): The Library class can be extended with new functionality (such as adding new commands or storage options) without modifying the existing code.
- Liskov Substitution Principle (LSP): The LibraryInterface interface ensures that any class implementing it can replace the Library class without disrupting the program.
- Interface Segregation Principle (ISP): The LibraryInterface is used to specify the methods necessary for working with a library, ensuring clear and specific responsibilities.
- Dependency Inversion Principle (DIP): The LibraryManager class depends on abstractions (LibraryInterface) rather than concrete classes, allowing for flexibility in how libraries are implemented.

*Run the code:*
You can run the script directly from the command line:
python task_1.py

*How It Works:*
The user interacts with the library through the command line by entering commands like:
- add to add a new book.
- remove to remove a book by title.
- show to display all books in the library.
- exit to exit the program.