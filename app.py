import streamlit as st

st.set_page_config(page_title="15 Project Icons", page_icon="🎨")

st.markdown(
    f"""
    <style>
        body {{
            background-color: #c7522a;
        }}
        .button {{
            background-color: #008585;
            color: #e5c185;
            width: 100%;
            height: 50px;
            border-radius: 10px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
        }}
        .button:hover {{
            background-color: #006666;
        }}
        .disabled {{
            background-color: #008585;
            color: #e5c185;
            width: 100%;
            height: 50px;
            border-radius: 10px;
            font-size: 16px;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.5;
            cursor: not-allowed;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color: #b8cdab; text-align: center;'>Welcome to the 15 Project Icons Page</h1>",
            unsafe_allow_html=True)

projects = [
    ("First Project", "https://pythoncourseradiodata-awpmjesxcvc84rlwx6kk5m.streamlit.app/"),
    ("Second Project", ""),
    ("Third Project", ""),
    ("Fourth Project", ""),
    ("Fifth Project", ""),
    ("Sixth Project", ""),
    ("Seventh Project", ""),
    ("Eighth Project", ""),
    ("Ninth Project", ""),
    ("Tenth Project", ""),
    ("Eleventh Project", ""),
    ("Twelfth Project", ""),
    ("Thirteenth Project", ""),
    ("Fourteenth Project", ""),
    ("Fifteenth Project", "")
]

col1, col2, col3 = st.columns(3)

for i, (project_name, project_link) in enumerate(projects):
    if project_link:
        col1.markdown(f"<a href='{project_link}' target='_blank' class='button'>{project_name}</a>", unsafe_allow_html=True)
    else:
        col1.markdown(f"<div class='disabled'>{project_name}</div>", unsafe_allow_html=True)

    if i % 5 == 0:
        col1, col2, col3 = st.columns(3)
