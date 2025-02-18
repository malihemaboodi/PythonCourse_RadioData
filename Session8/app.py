import streamlit as st

# Define the alphabet and vowels
alphabet = list("abcdefghijklmnopqrstuvwxyz")
vowels = ['a', 'e', 'i', 'o', 'u']


def encrypt(original_text, decode_or_encode):
    final_text = ""

    for letter in original_text:
        if letter not in alphabet:  # Keep spaces and special characters unchanged
            final_text += letter
            continue

        if decode_or_encode == "encode":
            if letter in vowels:
                shifted_position = vowels.index(letter) + 1
                if shifted_position >= len(vowels):
                    shifted_position = 0
                final_text += vowels[shifted_position]
            else:
                shifted_position = alphabet.index(letter) - 1
                if shifted_position < 0:
                    shifted_position = 0
                final_text += alphabet[shifted_position]

        else:  # "decode" mode
            if letter in vowels:
                shifted_position = vowels.index(letter) - 1
                if shifted_position < 0:
                    shifted_position = len(vowels) - 1
                final_text += vowels[shifted_position]
            else:
                shifted_position = alphabet.index(letter) + 1
                if shifted_position >= len(alphabet):
                    shifted_position = len(alphabet) - 1
                final_text += alphabet[shifted_position]

    return final_text


# 🎨 Streamlit UI
st.title("🔐 Text Encryption & Decryption")
st.write("This tool encrypts or decrypts your text based on a special algorithm.")

# User input
text = st.text_area("📝 Enter your text:", "")
direction = st.radio("📌 Choose an option:", ["encode", "decode"])

if st.button("🚀 Run!"):
    if text.strip() == "":
        st.warning("❌ Please enter some text!")
    else:
        result = encrypt(text.lower(), direction)
        st.success(f"🔑 **{direction.capitalize()}d result:**")
        st.code(result, language="plaintext")
