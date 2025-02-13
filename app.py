import streamlit as st

st.set_page_config(page_title="15 Project Icons", page_icon="🎨")

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
            margin-bottom: 10px; /* فاصله بین دکمه‌ها */
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
            margin-bottom: 10px; /* فاصله بین دکمه‌ها */
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

cols = st.columns(3)  # دکمه‌ها در سه ستون قرار می‌گیرند.

for i, (project_name, project_link) in enumerate(projects):
    col = cols[i % 3]  # انتخاب ستون مناسب

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
