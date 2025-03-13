# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return "Some sound"
    
    def __str__(self):
        return f"{self.name} is a {self.species}."

# Derived class 1
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the base class constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    def speak(self):
        return "Bark!"
    
    def __str__(self):
        return f"{self.name} is a {self.breed} dog."

# Derived class 2 (Cat)
class Cat(Animal):
    def __init__(self, name, breed):
        # Call the base class constructor
        super().__init__(name, "Cat")
        self.breed = breed
    
    def speak(self):
        return "Meow!"
    
    def __str__(self):
        return f"{self.name} is a {self.breed} cat."

# Derived class 3 (Siamese cat, which inherits from Cat)
class Siamese(Cat):
    def __init__(self, name):
        # Call the base class constructor, specifying "Siamese" as the breed
        super().__init__(name, "Siamese")
    
    def speak(self):
        return "Siamese meow!"
    
    def __str__(self):
        return f"{self.name} is a Siamese cat."
