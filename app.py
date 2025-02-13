import streamlit as st

st.set_page_config(page_title="15 Project Icons", page_icon="🎨")

st.markdown(
    f"""
    <style>
        body {{
            background-color: #c7522a;
        }}
        .custom-button {{
            display: block;
            background-color: #008585;
            color: #e5c185;
            width: 100%;
            height: 50px;
            border-radius: 10px;
            font-size: 16px;
            text-align: center;
            line-height: 50px;
            text-decoration: none;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }}
        .custom-button:hover {{
            background-color: #006666;
        }}
        .disabled-button {{
            background-color: #008585;
            color: #e5c185;
            width: 100%;
            height: 50px;
            border-radius: 10px;
            font-size: 16px;
            text-align: center;
            line-height: 50px;
            font-weight: bold;
            border: none;
            cursor: not-allowed;
            opacity: 0.6;
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
        # دکمه‌ی فعال که استایل مشابه دکمه‌ی غیرفعال دارد.
        col.markdown(
            f"<a href='{project_link}' class='custom-button' target='_blank'>{project_name}</a>",
            unsafe_allow_html=True
        )
    else:
        # دکمه‌ی غیرفعال با استایل مشابه دکمه‌ی فعال
        col.markdown(f"<div class='disabled-button'>{project_name}</div>", unsafe_allow_html=True)
