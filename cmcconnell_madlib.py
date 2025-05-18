"""Cameron McConnell
Mad Lib Game
05/13/2025
____________
This is a fun game that asks the user for random
words and uses them to create a silly story.
It demonstrates the use of input, variables, and
string interpolation (f-strings). """

print("Hello!")
animal1 = input("Name an animal: ")
instrument = input("Name an instrument: ")
animal2 = input("Name another animal: ")
planet = input("Name a planet: ")
animal3 = input("Give me the last animal: ")
utensil1 = input("Name an utensil: ")
utensil2 = input("Give me the last utensil: ")

print(" ")
print("Here is your mad lib story!")
print(" ")
print("Hey diddle diddle")
print(f"The {animal1} and the {instrument}")
print(f"The {animal2} jumped over {planet}")
print(f"The little {animal3} laughed")
print("To see such a sport")
print(f"And the {utensil1} ran away with the {utensil2}")
