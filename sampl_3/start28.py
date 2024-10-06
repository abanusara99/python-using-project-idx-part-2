class digit: # digit is classname - class classname  
    """A simple class to store and display a value."""
    
    def __init__(self, value):
        self.value = value  # Instance attribute
    
    def display(self):
        print(f"The value is: {self.value}")

# Example usage
my_instance = digit(600)  #calling the classname - 
my_instance.display()       # printing the data of class