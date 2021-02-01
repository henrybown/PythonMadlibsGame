import random

# Take user input, and store it in variables
name = input("Enter a name: ")
animal1 = input("Enter an animal: ")
animal2 = input("Enter a 2nd animal: ")
city = input("Enter a city: ")
color = input("Enter a color: ")
body_part = input("Enter a body part: ")

# Concatenate the color and 2nd animal to make the 2nd character's name
animal2 = color + " " + animal2

# Generates random number between 1 and 10, then creates string based on if it rolled 1 or not
bites = random.randint(1,10)
if bites == 1:
    bites = str(bites) + " bite"
else:
    bites = str(bites) + " bites"

# Print out a story, with the variables entered previously
print(name + " was a " + animal1 + " who lived in " + city)
print("Unfortunately, " + animal2 + " really like eating " + animal1 + " curry")
print(name + " was walking to the shop, when " + animal2 + " picked him up with it's " + body_part)
print("The " + animal1 + " was minced and swallowed in " + bites + ", with some ketchup")
print("Luckily for " + name + ", " + animal2 + " was shot, and " + name + " managed to climb out of its mouth again")
print("Then " + name + " got hit by a train")
print("The end")