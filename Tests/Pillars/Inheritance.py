# Test Class to demonstrate inheritance
class AnimalTest:
    @staticmethod
    def test_animal_classes():
        # Create instances of different animal classes
        dog = Dog("Buddy", "Golden Retriever")
        cat = Cat("Whiskers", "Siamese")
        siamese_cat = Siamese("Leo")  # A specific type of Cat (Siamese)

        # Test the speak method and __str__ method of each class
        print(dog.speak())  # Expected: "Bark!"
        print(cat.speak())  # Expected: "Meow!"
        print(siamese_cat.speak())  # Expected: "Siamese meow!"

        print(dog)  # Expected: "Buddy is a Golden Retriever dog."
        print(cat)  # Expected: "Whiskers is a Siamese cat."
        print(siamese_cat)  # Expected: "Leo is a Siamese cat."

# Running the test
AnimalTest.test_animal_classes()
