"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the Animal Kingdom program from Lab 1 to include polymorphism,
               demonstrating method overriding in derived classes.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Paste your base class Animal and the derived classes from Lab 1 here.
# Modify the classes to demonstrate polymorphism through method overriding.
class Animal:
    def __init__(self, name, age, habitat,):
        self.name = name
        self.age = age
        self.habitat = habitat
    
    def eat(self):
        return (f"{self.name} is eating")
    
    def sleep(self):
        return (f"{self.name} is sleeping")
    
    def display_info(self):
       return f"This {self.name} is a {self.age} yr old animal that lives in {self.habitat}"

class Bird(Animal):
    def __init__(self, name, age, habitat, colour):
            super().__init__(name, age, habitat)
            self.colour = colour
        
    def fly(self):
        print(f"{self.name} is flying")
        
    def display_info(self):
        return f"This {self.name} is a {self.colour}, {self.age} yr old bird that lives in {self.habitat}"
        
class Fish(Animal):
    def __init__(self, name, age, habitat, speed):
        super().__init__(name, age, habitat)
        self.speed = speed
        
    def swim(self):
        print(f"{self.name} is swimming")
        
    def display_info(self):
        return f"This {self.name} is a {self.speed}, {self.age} yr old fish that lives in {self.habitat}"

Pigeon = Bird("Pigeon", "3", "New York", "Grey",)
Duck = Bird("Duck", "4", "A Pond", "Grey and Green",)
Salmon = Fish("Salmon", "1", "A River", "Fast")


# Each derived class should override at least one method from the Animal class.
# For instance, you might want to override a 'make_sound' method to reflect the specific sound each animal makes.

# Create at least two instances of your derived classes
# Call the overridden methods on the instances.

zoo = [Pigeon, Duck, Salmon]

for Animal in zoo:
    print(Animal.display_info())


