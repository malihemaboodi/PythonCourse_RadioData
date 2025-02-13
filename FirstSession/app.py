import streamlit as st

# Welcome message
# This will print a welcoming message to the user when the program starts
st.title("Funny Sport Name Generator")
st.write("Welcome to the Funny Sport Name Generator!")

# Ask the user for a sport-related item or activity
# The user will input the name of a sport-related item (e.g., a ball, running, jumping, etc.)
# We capture this input in the variable 'sport_gear'
sport_gear = st.text_input("What is the name of a sport-related item or activity?")

# Ask the user for a funny thing (animal, object, or adjective)
# The user will input the name of a funny thing (e.g., a panda, ninja, banana, etc.)
# We capture this input in the variable 'funny_thing'
funny_thing = st.text_input("What is the name of a funny animal, object, or adjective?")

# Combine the inputs and generate a funny sport name
# This step combines the sport-related item and the funny thing entered by the user
# We use string concatenation to join these two inputs with a space in between
if sport_gear and funny_thing:  # Only generate the name if both inputs are provided
    st.write(f"Your new sport name could be: {sport_gear} {funny_thing}!")
