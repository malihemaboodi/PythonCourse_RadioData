import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="Funny Sport Name Generator", page_icon="⚽")

# Add a header
st.markdown("""
    <h1 style="text-align: center; color: #4CAF50;">Funny Sport Name Generator</h1>
    <p style="text-align: center; color: #555;">Create your own fun sport name with just a few inputs!</p>
""", unsafe_allow_html=True)

# Add an image
st.image("../assets/sport_logo.jpg", use_container_width=True)




# Ask the user for a sport-related item or activity
sport_gear = st.text_input("What is the name of a sport-related item or activity?", placeholder="e.g., Ball, Running, Swimming")

# Ask the user for a funny thing (animal, object, or adjective)
funny_thing = st.text_input("What is the name of a funny animal, object, or adjective?", placeholder="e.g., Panda, Ninja, Banana")

# Check if the inputs are filled and display the result
if sport_gear and funny_thing:
    st.markdown(f"""
        <h2 style="text-align: center; color: #FF6347;">Your new sport name could be:</h2>
        <h3 style="text-align: center; color: #FFA500; font-size: 30px;">{sport_gear} {funny_thing}!</h3>
    """, unsafe_allow_html=True)
else:
    st.write("Please enter both the sport-related item and the funny thing to generate your name.")
