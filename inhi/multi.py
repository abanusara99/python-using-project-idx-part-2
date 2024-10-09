class Animal:  # Base class
    def speak(self):
        return "Animal speaks"

class Canine:  # Another base class
    def bark(self):
        return "Bark!"

class Dog(Animal, Canine):  # Derived class
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog()
print(dog.speak())  
print(dog.bark())   