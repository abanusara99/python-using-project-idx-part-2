class Animal:  # Base class
    def speak(self):
        return "Animal speaks"

class Mammal(Animal):  # Intermediate derived class
    def walk(self):
        return "Mammal walks"

class Dog(Mammal):  # Derived class
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog()
print(dog.speak())  
print(dog.walk())   