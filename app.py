import streamlit as st

st.set_page_config(page_title="Python Course at Radio.Data", page_icon="🐍")

st.markdown(
    f"""
    <style>
        body {{
            background-color: #c7522a;
        }}
        .button-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
        }}
        .custom-button {{
            display: block;
            background-color: #008585;
            color: #e5c185;
            width: 90%;
            height: 50px;
            border-radius: 10px;
            font-size: 16px;
            text-align: center;
            line-height: 50px;
            text-decoration: none;
            font-weight: bold;
            border: none;
            cursor: pointer;
            margin-bottom: 10px; 
        }}
        .custom-button:hover {{
            background-color: #006666;
        }}
        .disabled-button {{
            background-color: #008585;
            color: #e5c185;
            width: 90%;
            height: 50px;
            border-radius: 10px;
            font-size: 16px;
            text-align: center;
            line-height: 50px;
            font-weight: bold;
            border: none;
            cursor: not-allowed;
            opacity: 0.6;
            margin-bottom: 10px; 
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color: #f37324; text-align: center;'>Welcome to the Python Course at Radio.Data</h1>",
            unsafe_allow_html=True)

projects = [
    ("First Project", "https://pythoncourseradiodata-awpmjesxcvc84rlwx6kk5m.streamlit.app/"),
    ("Second Project", "https://pythoncourseradiodatabudgetmanagementprogram.streamlit.app/"),
    ("Third Project", "https://pythoncourseradiodatathirdsession.streamlit.app/"),
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

cols = st.columns(3)

for i, (project_name, project_link) in enumerate(projects):
    col = cols[i % 3]

    if project_link:
        col.markdown(
            f"<div class='button-container'><a href='{project_link}' class='custom-button' target='_blank'>{project_name}</a></div>",
            unsafe_allow_html=True
        )
    else:
        col.markdown(
            f"<div class='button-container'><div class='disabled-button'>{project_name}</div></div>",
            unsafe_allow_html=True
        )
