import streamlit as st
import random

st.set_page_config(page_title="Fun Animal Challenge", page_icon="🐾")

st.markdown("""
    <h1 style="text-align: center; color: #4CAF50;">🦁 Fun Animal Challenge 🐱</h1>
    <p style="text-align: center; color: #555;">Choose an animal and see if you can beat the computer's choice! 🐭</p>
""", unsafe_allow_html=True)

animals = ["Lion", "Cat", "Mouse"]

user_choice = st.selectbox("Choose your animal:", animals)

if user_choice:
    computer_choice = random.choice(animals)
    st.write(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        st.markdown(f"<h3 style='text-align: center; color: #FF6347;'>It's a Draw! You both chose {user_choice}!</h3>", unsafe_allow_html=True)
    elif (user_choice == "Lion" and computer_choice == "Cat") or \
         (user_choice == "Cat" and computer_choice == "Mouse") or \
         (user_choice == "Mouse" and computer_choice == "Lion"):
        st.markdown(f"<h3 style='text-align: center; color: #32CD32;'>You Win! Your {user_choice} beats the computer's {computer_choice}!</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='text-align: center; color: #FF4500;'>You Lose! The computer's {computer_choice} beats your {user_choice}!</h3>", unsafe_allow_html=True)
