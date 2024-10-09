class Animal:  # Base class
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Derived class 1
    def speak(self):
        return "Woof!"

class Cat(Animal):  # Derived class 2
    def speak(self):
        return "Meow!"

# Example usage
dog = Dog()
cat = Cat()
print(dog.speak()) 
print(cat.speak())   