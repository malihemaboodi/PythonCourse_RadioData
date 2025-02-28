import streamlit as st

# Dictionary of predefined questions and answers
qa_dict = {
    "What are the phases of the analysis of accounting transactions?":
        "The phases of the analysis of accounting transactions are:\n"
        "a) Setting up possible filters for the transactions.\n"
        "b) Defining the types of analysis with corresponding levels of grouping.\n"
        "c) Querying and printing the analysis of the transactions.",

    "What does the function allow to do?":
        "The function allows you to set different types of analysis by specifying how many and which fields from the accounting "
        "transactions database will act as grouping keys.",

    "How can the filters be defined?":
        "The filters on the accounting transactions can be defined through the standard user filter creation functionality. "
        "You can select generic filters or those defined by the current user.",

    "What does the second page allow to do?":
        "The second page allows you to specify the key fields for grouping the transactions, as well as the options for "
        "decoding and excluding null values.",

    "What is required on the first page of the analysis function?":
        "On the first page of the analysis function, the following are required: the code (5 alphanumeric characters), "
        "the analysis title, the filter on the transactions, the number of groupings, and the currency type."
}


# Function to handle user question and display the answer
def handle_question(question):
    # Check if the question is in the dictionary
    return qa_dict.get(question, "Sorry, I don't have an answer for that.")


# Streamlit UI
st.set_page_config(page_title="AI Assistant for Accounting", page_icon=":robot_face:", layout="wide")

# Title and Subheader
st.markdown("<h1 style='text-align: center;'>AI Assistant for Accounting Transactions</h1>", unsafe_allow_html=True)
st.subheader("Ask me anything related to accounting analysis!")

# Input box for user question with some custom styling
user_question = st.text_input("Type your question here:", placeholder="E.g., What are the phases of analysis?")

# Styling the container
st.markdown(
    """
    <style>
    .css-1d391kg {
        padding: 20px;
        background-color: #f0f4f7;
        border-radius: 10px;
        font-size: 18px;
    }
    .css-1b6bcm5 {
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display answer based on question
if user_question:
    answer = handle_question(user_question)
    # Display question and answer in a box with some padding and color
    st.markdown(
        f"<div class='css-1d391kg'><p><span class='css-1b6bcm5'>Question:</span> {user_question}</p><p><span class='css-1b6bcm5'>Answer:</span> {answer}</p></div>",
        unsafe_allow_html=True)

