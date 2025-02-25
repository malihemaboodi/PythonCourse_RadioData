import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="🏋️‍♂️ Weight Loss Challenge 💪", layout="centered")

# Title and description
st.title("🏋️‍♂️ **Weight Loss Challenge** 💪")
st.markdown("""
📢 **Every month, the gym rewards the participant with the highest weight loss!**  
🏆 **Are you ready to break the record and win?!** 😍  
""")

# Store participant data in session state
if "bids" not in st.session_state:
    st.session_state.bids = {}

# Form for user input
with st.form("weight_loss_form"):
    name = st.text_input("👤 Enter your name:")
    initial_weight = st.number_input("⚖️ Initial weight (kg):", min_value=1)
    current_weight = st.number_input("📉 Current weight (kg):", min_value=1)
    submitted = st.form_submit_button("➕ Submit")

    # Validate input and store data
    if submitted:
        if name and initial_weight > current_weight:
            st.session_state.bids[name] = {"start": initial_weight, "current": current_weight}
            st.success(f"✅ {name} has been successfully registered!")
        else:
            st.error("❌ Please enter a name and ensure the current weight is lower than the initial weight.")

# Display participant list
if st.session_state.bids:
    st.markdown("### 📋 **Participants so far:**")
    df = pd.DataFrame([
        {"Name": name, "Initial Weight (kg)": data["start"], "Current Weight (kg)": data["current"], "Weight Loss (kg)": data["start"] - data["current"]}
        for name, data in st.session_state.bids.items()
    ])
    st.dataframe(df, use_container_width=True)

    # Find the winner
    winner = max(st.session_state.bids.items(), key=lambda x: x[1]["start"] - x[1]["current"])
    winner_name, winner_data = winner
    max_loss = winner_data["start"] - winner_data["current"]

    # Display winner
    st.markdown(f"## 🏆 **Current Leader:** {winner_name} with **{max_loss} kg lost!** 🎉")

    # Show weight loss chart
    st.bar_chart(df.set_index("Name")["Weight Loss (kg)"])

    # Reset button to restart the challenge
    if st.button("🔄 Restart Challenge"):
        st.session_state.bids = {}
        st.experimental_rerun()
