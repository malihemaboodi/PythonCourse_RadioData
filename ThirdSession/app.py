import streamlit as st
# Set the page title and icon
st.set_page_config(page_title="Driving Test", page_icon="🚗")
# Title and description
st.title("🚗 Driving Test: Will You Get Your License? 🚦")
st.markdown("""
You are taking a driving test, and you must make the right decisions to pass and get your license! Every choice you make can bring you closer to passing or failing the test.
""")

# Step 1
st.subheader("1️⃣ You are behind the wheel. The traffic light turns yellow. What do you do?")
step_1 = st.radio("Choose your action:", ["Wait (You slow down and stop)", "Speed up (You rush through)"])

if step_1 == "Wait (You slow down and stop)":
    st.success("✅ Correct! You slowed down and stopped.")
    # Step 2
    st.subheader("2️⃣ You approach an intersection. A pedestrian is crossing the street. What do you do?")
    step_2 = st.radio("Choose your action:", ["Stop (You let them pass)", "Keep going (You don’t stop)"])

    if step_2 == "Stop (You let them pass)":
        st.success("✅ Correct! You let the pedestrian pass.")
        # Step 3
        st.subheader("3️⃣ At the end of the test, the instructor asks you:")
        st.markdown('"On a slippery road, how much distance should you keep from the car ahead?"')
        step_3 = st.radio("Choose your answer:", ["More than usual", "Same as usual", "Any other answer"])

        if step_3 == "More than usual":
            st.success("✅ Correct! You passed the test! 🎉")
            st.balloons()  # Show balloons for success
        else:
            st.error("❌ Incorrect! You failed. 😢")
    else:
        st.error("❌ Incorrect! You didn’t stop for the pedestrian.")
else:
    st.error("❌ Incorrect! You rushed through the light.")
