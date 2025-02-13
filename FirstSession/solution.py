# Welcome message
# This will print a welcoming message to the user when the program starts
print("Welcome to the Funny Sport Name Generator!")



# Ask the user for a sport-related item or activity
# The user will input the name of a sport-related item (e.g., a ball, running, jumping, etc.)
# We capture this input in the variable 'sport_gear'
sport_gear = input("What is the name of a sport-related item or activity?\n")

# Ask the user for a funny thing (animal, object, or adjective)
# The user will input the name of a funny thing (e.g., a panda, ninja, banana, etc.)
# We capture this input in the variable 'funny_thing'

funny_thing = input("What is the name of a funny animal, object, or adjective?\n")

# Combine the inputs and generate a funny sport name
# This step combines the sport-related item and the funny thing entered by the user
# We use string concatenation to join these two inputs with a space in between
print("Your new sport name could be: " + sport_gear + " " + funny_thing + "!")