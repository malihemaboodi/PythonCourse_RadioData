import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="Funny Sport Name Generator", page_icon="⚽")

# Custom CSS for styling
st.markdown(
    f"""
    <style>
        body {{
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
        }}
        h1 {{
            text-align: center;
            color: #4CAF50;
            font-size: 3em;
            margin-top: 50px;
            font-weight: bold;
        }}
        p {{
            text-align: center;
            color: #555;
            font-size: 1.2em;
        }}
        .input-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 30px;
        }}
        .input-field {{
            width: 80%;
            padding: 15px;
            margin-bottom: 20px;
            font-size: 1.1em;
            border-radius: 10px;
            border: 2px solid #4CAF50;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            outline: none;
            transition: all 0.3s ease;
        }}
        .input-field:focus {{
            border-color: #FFA500;
            box-shadow: 0 4px 8px rgba(255, 165, 0, 0.5);
        }}
        .generate-button {{
            background-color: #FF6347;
            color: white;
            font-size: 1.2em;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease, transform 0.3s ease;
        }}
        .generate-button:hover {{
            background-color: #FF4500;
            transform: scale(1.05);
        }}
        .generate-button:active {{
            background-color: #E63A2B;
        }}
        .result {{
            text-align: center;
            color: #FF6347;
            font-size: 2em;
            margin-top: 30px;
            font-weight: bold;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add a header and description
st.markdown("""
    <h1>Funny Sport Name Generator</h1>
    <p>Create your own fun sport name with just a few inputs!</p>
""", unsafe_allow_html=True)

# Ask the user for a sport-related item or activity
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
sport_gear = st.text_input("What is the name of a sport-related item or activity?", placeholder="e.g., Ball, Running, Swimming", key="sport_gear", label_visibility="collapsed", max_chars=30)

# Ask the user for a funny thing (animal, object, or adjective)
funny_thing = st.text_input("What is the name of a funny animal, object, or adjective?", placeholder="e.g., Panda, Ninja, Banana", key="funny_thing", label_visibility="collapsed", max_chars=30)

st.markdown("</div>", unsafe_allow_html=True)

# Check if the inputs are filled and display the result
if sport_gear and funny_thing:
    st.markdown(f"""
        <div class='result'>
            Your new sport name could be:<br><span style="font-size: 2.5em; color: #FFA500;">{sport_gear} {funny_thing}!</span>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class='result'>
            Please enter both the sport-related item and the funny thing to generate your name.
        </div>
    """, unsafe_allow_html=True)

# Optional: Add a button to generate another name (if desired)
# st.button("Generate Another Name", key="generate_button", on_click=generate_name_function)
