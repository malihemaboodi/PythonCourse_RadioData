import streamlit as st

st.set_page_config(page_title="15 Project Icons", page_icon="🎨")

st.markdown(
    f"""
    <style>
        body {{
            background-color: #c7522a;
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
    button_style = f"background-color: #008585; color: #e5c185; width: 100%; height: 50px; border-radius: 10px; font-size: 16px;"

    if project_link:
        if col1.button(project_name, key=i, help=f"Go to {project_name}"):
            st.write(f"Redirecting to {project_name}...")
            st.markdown(f"[Click here to visit]({project_link})")
    else:
        col1.markdown(f"<button style='{button_style}' disabled>{project_name}</button>", unsafe_allow_html=True)

    if i % 5 == 0:
        col1, col2, col3 = st.columns(3)
