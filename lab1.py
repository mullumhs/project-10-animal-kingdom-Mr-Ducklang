"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.
class Animal:
    def __init__(self, name, age, habitat,):
        
        self.name = name
        self.age = age
        self.habitat = habitat
    
    def eat(self):
        return (f"{self.name} is eating")
    
    def sleep(self):
        return (f"{self.name} is sleeping")

# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.

class Bird(Animal):
    def __init__(self, name, age, habitat,):
        super().__init__(name, age, habitat)
        
    def fly(self):
        print(f"{self.name} is flying")
        
class Fish(Animal):
    def __init__(self, name, age, habitat,):
        super().__init__(name, age, habitat)
        
    def swim(self):
        print(f"{self.name} is swimming")
        

# Create at least two instances of the Animal derived classes with different data.

Pigeon = Bird("Pigeon", "3", "New York")
Duck = Bird("Duck", "4", "Pond")

Salmon = Fish("Salmon", "1", "River")

# Write code that prints out the details of each animal and calls their specific behaviors.

print(Pigeon.fly())
print(Pigeon.sleep())

print(Salmon.swim())
print(Salmon.sleep()) 
