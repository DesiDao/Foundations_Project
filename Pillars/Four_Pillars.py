from abc import ABC, abstractmethod

# Base Class: Animal (Encapsulation, Abstraction)
class Animal(ABC):
    def __init__(self, name, species):
        # Encapsulation: Attributes are bundled with methods
        self.name = name
        self.species = species
    
    def make_sound(self):
        # Abstraction: Hides implementation details of sound-making
        raise NotImplementedError("Subclass must implement abstract method")
    
    @abstractmethod
    def get_age(self):
        # Abstraction with @abstractmethod
        pass
    
    def get_description(self):
        return f"{self.name} is a {self.species}"

# Derived Class: Dog (Inheritance, Polymorphism)
class Dog(Animal):
    def __init__(self, name, breed, age):
        # Inheritance: Dog class inherits from Animal class
        super().__init__(name, "Dog")  # Call the base class constructor
        self.breed = breed
        self.age = age
    
    def make_sound(self):
        # Polymorphism: Overriding the make_sound method
        return f"{self.name} says Woof!"
    
    def get_age(self):
        # Implement the abstract method get_age
        return f"{self.name} is {self.age} years old"
    
    def get_description(self):
        return f"{self.name} is a {self.breed} and belongs to the species {self.species}"

# Derived Class: Cat (Inheritance, Polymorphism)
class Cat(Animal):
    def __init__(self, name, color, age):
        # Inheritance: Cat class inherits from Animal class
        super().__init__(name, "Cat")  # Call the base class constructor
        self.color = color
        self.age = age
    
    def make_sound(self):
        # Polymorphism: Overriding the make_sound method
        return f"{self.name} says Meow!"
    
    def get_age(self):
        # Implement the abstract method get_age
        return f"{self.name} is {self.age} years old"
    
    def get_description(self):
        return f"{self.name} is a {self.color} cat"
