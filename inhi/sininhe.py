class Animal:  # Base class
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Derived class
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog()
print(dog.speak())  