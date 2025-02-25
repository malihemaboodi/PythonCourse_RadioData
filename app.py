import streamlit as st

# Set page configuration
st.set_page_config(page_title="Python Course at Radio.Data", page_icon="🐍")

# Custom CSS for styling
st.markdown(
    f"""
    <style>
        body {{
            background-color: #f4e1d2;
            font-family: 'Arial', sans-serif;
        }}
        h1 {{
            color: #f37324;
            text-align: center;
            font-size: 3em;
            margin-top: 50px;
        }}
        .button-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            margin-bottom: 20px;
        }}
        .custom-button {{
            display: block;
            background-color: #008585;
            color: #e5c185;
            width: 90%;
            height: 60px;
            border-radius: 15px;
            font-size: 18px;
            text-align: center;
            line-height: 60px;
            text-decoration: none;
            font-weight: bold;
            border: none;
            cursor: pointer;
            margin-bottom: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease, transform 0.3s ease;
        }}
        .custom-button:hover {{
            background-color: #006666;
            transform: scale(1.05);
        }}
        .custom-button:active {{
            background-color: #004d4d;
        }}
        .disabled-button {{
            background-color: #d4d4d4;
            color: #a1a1a1;
            width: 90%;
            height: 60px;
            border-radius: 15px;
            font-size: 18px;
            text-align: center;
            line-height: 60px;
            font-weight: bold;
            border: none;
            cursor: not-allowed;
            opacity: 0.7;
            margin-bottom: 15px;
        }}
        .header-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 50px;
        }}
        .projects-container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-evenly;
            margin-top: 30px;
        }}
        .project-col {{
            flex: 0 0 30%;
            margin-bottom: 20px;
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<div class='header-container'><h1>Welcome to the Python Course at Radio.Data</h1></div>", unsafe_allow_html=True)

# Project List
projects = [
    ("First Project", "https://pythoncourseradiodata-6xf3uua82hmirovuxexdwc.streamlit.app/"),
    ("Second Project", "https://pythoncourseradiodata-nh2qnx8ryz6blvw2opncee.streamlit.app/"),
    ("Third Project", "https://pythoncourseradiodata-myke92jezncls7fnn66xj2.streamlit.app/"),
    ("Fourth Project", "https://pythoncourseradiodata-5hteysbkrtky4mcneryfpw.streamlit.app/"),
    ("Fifth Project", "https://pythoncourseradiodata-7iu8nu679rkuvwhhut24cv.streamlit.app/"),
    ("Sixth Project", ""),
    ("Seventh Project", "https://pythoncourseradiodata-d7gy86s7bcga9whlc3q8yw.streamlit.app/"),
    ("Eighth Project", "https://pythoncourseradiodata-kfr3xsxfwvewsbngzxfoxm.streamlit.app/"),
    ("Ninth Project", "https://pythoncourseradiodata-kyoqzq4doqeg6b3ddrueyk.streamlit.app/"),
    ("Tenth Project", ""),
    ("Eleventh Project", ""),
    ("Twelfth Project", ""),
    ("Thirteenth Project", ""),
    ("Fourteenth Project", ""),
    ("Fifteenth Project", "")
]

# Container for the project buttons
st.markdown("<div class='projects-container'>", unsafe_allow_html=True)

# Loop through projects and display buttons
for project_name, project_link in projects:
    if project_link:
        st.markdown(
            f"<div class='project-col'><a href='{project_link}' class='custom-button' target='_blank'>{project_name}</a></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='project-col'><div class='disabled-button'>{project_name}</div></div>",
            unsafe_allow_html=True
        )

# Close the container
st.markdown("</div>", unsafe_allow_html=True)
