import streamlit as st
import random

# Funny comments for wrong guesses
funny_comments = [
    "What the hell baba jan!! Guesset wrooooong bod! 😂",
    "Bro, are you even trying?!! 🤨",
    "In guess ghalat mahshariiii! To maghzet che khabare? 👀",
    "Man daram ghargh misham 😭 plzzzz guess right!",
    "Baba ye khoorde be khodet biya 😩",
    "Ajab badbakhtam man!!!! agha dige mishe guess dorost bezani?!! 😵‍💫"
]

# List of words
word_list = ["octopus", "whale", "dolphin", "shark", "jellyfish"]

# Initialize game state
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.num_lives = 5
    st.session_state.correct_letters = []
    st.session_state.display_word = "-" * len(st.session_state.chosen_word)
    st.session_state.game_over = False

# UI Design
st.title("🐠 Save The Poor Fish! 🏝️")
st.markdown("## 🎮 Guess the Word and Rescue the Fish!")
# st.image("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif", use_container_width=True)

st.markdown(f"### 🌊 Word Status: `{st.session_state.display_word}`")
st.markdown(f"### ❤️ Lives Left: `{st.session_state.num_lives}/5`")

if st.session_state.game_over:
    if st.session_state.num_lives > 0:
        st.success(f"🎉 YOU WON! The word was `{st.session_state.chosen_word}`! The fish is SAFE! 🐟🥳")
    else:
        st.error(f"💀 GAME OVER! The word was `{st.session_state.chosen_word}`. The fish is... gone 😭")
        st.image("https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif", use_container_width=True)
else:
    user_guess = st.text_input("🎯 Enter a letter:", max_chars=1).lower()
    if st.button("Guess!") and user_guess:
        if user_guess in st.session_state.correct_letters:
            st.warning("🤨 Baba in ro ghablan gofti!! Ye harf ro 2 bar nagoooo!")
        elif user_guess in st.session_state.chosen_word:
            st.session_state.correct_letters.append(user_guess)
            st.success("✅ Oooof boos behet baba 🥳!")
        else:
            st.session_state.num_lives -= 1
            st.error(random.choice(funny_comments))

        # Update displayed word
        st.session_state.display_word = "".join([
            lett if lett in st.session_state.correct_letters else "-"
            for lett in st.session_state.chosen_word
        ])

        # Check game status
        if "-" not in st.session_state.display_word:
            st.session_state.game_over = True
        elif st.session_state.num_lives == 0:
            st.session_state.game_over = True

if st.button("🔄 Restart Game"):
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.num_lives = 5
    st.session_state.correct_letters = []
    st.session_state.display_word = "-" * len(st.session_state.chosen_word)
    st.session_state.game_over = False
    st.experimental_rerun()
