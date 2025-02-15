import random
import streamlit as st

# Define character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['£','^','?','!', '#', '$', '%', '&', '(', ')', '*', '+']

# Title
st.title("Welcome to the Username 😎 Generator!")

# User inputs for the number of letters, symbols, and numbers
num_letters = st.number_input("How many letters would you like in your username?", min_value=1, max_value=20, value=5)
num_symbols = st.number_input("How many symbols would you like in your username?", min_value=1, max_value=5, value=1)
num_numbers = st.number_input("How many numbers would you like in your username?", min_value=1, max_value=5, value=2)

# Generate username
user_name = []

for _ in range(num_letters):
    user_name.append(random.choice(letters))

for _ in range(num_numbers):
    user_name.append(random.choice(numbers))

for _ in range(num_symbols):
    user_name.append(random.choice(symbols))

random.shuffle(user_name)

# Convert list to string
final_username = "".join(user_name)

# Display the result
st.subheader("Your generated username is:")
st.markdown(f"**{final_username}**", unsafe_allow_html=True)

# Extra Styling
st.markdown("""
    <style>
    .streamlit-expanderHeader {
        font-size: 1.5em;
        color: #4CAF50;
    }
    .stButton>button {
        background-color: #FF6347;
        color: white;
        font-size: 1.2em;
    }
    </style>
""", unsafe_allow_html=True)
