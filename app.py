import streamlit as st

st.set_page_config(page_title="15 Project Icons", page_icon="🎨")

st.markdown("**Welcome to the 15 Project Icons Page**")

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

cols = st.columns(3)

for i, (project_name, project_link) in enumerate(projects):
    col = cols[i % 3]  # دکمه‌ها را به تناوب در ستون‌های مختلف قرار می‌دهد
    if project_link:
        if col.button(project_name, key=i, help=f"Go to {project_name}"):
            st.write(f"Redirecting to {project_name}...")
            st.markdown(f"[Click here to visit]({project_link})")
    else:
        col.button(project_name, key=i, help=f"{project_name} has no link")
