class Dog: # classname1
    def __init__(self, name):
        self.name = name
        self.is_healthy = True
    
    def check_health(self):
        return "Healthy" if self.is_healthy else "Needs Attention"

class Doctor: # classname2
    def __init__(self, name):
        self.name = name
    
    def check_dog(self, dog):
        return f"Doctor {self.name} checks {dog.name}: {dog.check_health()}"
    
    def treat_dog(self, dog):
        dog.is_healthy = True
        return f"Doctor {self.name} treated {dog.name}. Now it's healthy!"

# Example usage
# my_dog and vet are object names
my_dog = Dog("Bob") # object name 1
vet = Doctor("Dr. Smith") # object name 2
print(vet.check_dog(my_dog))
print(vet.treat_dog(my_dog))