print("Welcome to the Space Adventure Generator!")
print("Answer the following questions to create your own space adventure story.")
spaceship_name = input("Enter the name of your spaceship: ")
planet_name = input("Enter the name of a planet: ")
alien_species = input("Enter the name of an alien species: ")
adjective = input("Enter an adjective to describe the aliens: ")
superpower = input("Enter a superpower you want to have: ")
object = input("Name an object you would bring to space: ")
#generating a story
space_story = f"""
Captain, welcome aboard the spaceship {spaceship_name}! Our mission is to explore the mysterious planet {planet_name}.
As we landed, we encountered a group of {adjective} aliens known as the {alien_species}.
Surprisingly, they weren’t hostile but instead offered us a gift—a device that granted us the power of {superpower}!

However, we soon realized that the {object} we brought along attracted the aliens' curiosity. 
To prevent intergalactic confusion, we shared its purpose with them, and they were fascinated by it.

Our journey to {planet_name} turned out to be an incredible adventure, and we formed a lasting friendship with the {adjective} {alien_species}.
"""
print("\nHere is your Space Adventure story:")
print(space_story)