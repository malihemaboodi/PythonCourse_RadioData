import streamlit as st


st.set_page_config(page_title="15 Project Icons", page_icon="🎨")


st.title("Welcome to the 15 Project Icons Page")


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
    icon_color = f"hsl({i * 24}, 100%, 50%)"


    if project_link:
        button = col1.button(project_name, key=i, help=f"Go to {project_name}")
        if button:
            st.write(f"Redirecting to {project_name}...")
            st.markdown(f"[Click here to visit]({project_link})")
    else:

        col1.button(project_name, key=i, help=f"{project_name} has no link")


    if i % 5 == 0:
        col1, col2, col3 = st.columns(3)
