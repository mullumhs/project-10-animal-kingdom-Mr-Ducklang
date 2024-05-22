"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Build a Zoo class to manage a collection of animals from the Animal
               Kingdom program. Demonstrate managing objects and class interactions.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Import your base class Animal and any derived classes (e.g., Bird, Fish) here from Lab 2.

from lab2 import Animal, Bird, Fish

# Define the Zoo class that can manage multiple Animal objects. It should have the following two methods:
# __init__ - Initialises a new Zoo instance with an empty list to hold animal objects.
# add_animal - Adds an animal to the zoo's list and confirms addition with a return message.
# You should then think of and implement at least one additional method for the Zoo class. E.g. feed_all

class Zoo:
    def __init__(self):
        self.animal = []
        
    def add_animal(self, animal):
        self.animal.append(animal)
        return f"{animal.name} added to zoo."
    
    def feed_all(self):
        print()
        for animal in self.animal:
            print(f"{animal.name} has been fed.")
            
        
    def clean_all(self):
        print()
        for animal in self.animal:
            print(f"{animal.name} has been cleaned")
            
        
    def display_all_info(self):
        print()
        for animal in self.animal:
            print(animal.display_info())



# Create instances of derived Animal classes and add them to the Zoo.

my_zoo = Zoo()

Sprat = Fish("Sprat", "2","In Coastal Waters","Slow" )
Eagle = Bird("Eagle", "7","In Forests","Brown" )


# Demonstrate the Zoo's functionality by calling its methods.

my_zoo.add_animal(Sprat)
my_zoo.add_animal(Eagle)

my_zoo.feed_all()
my_zoo.clean_all()
my_zoo.display_all_info()


