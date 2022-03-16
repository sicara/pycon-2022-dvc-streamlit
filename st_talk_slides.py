import streamlit as st
import streamlit_book as stb

from constants import CONFERENCE_LOGO_PATH, CONFERENCE_NAME

# Streamlit webpage properties
st.set_page_config(page_title=CONFERENCE_NAME, page_icon=str(CONFERENCE_LOGO_PATH))

st.sidebar.image(str(CONFERENCE_LOGO_PATH), width=50)
st.sidebar.write(CONFERENCE_NAME)

# Streamlit book properties
stb.set_book_config(
    menu_title="Menu",
    menu_icon="book",
    options=[
        "Introduction",
        "A DVC Pipeline to Train a Cats vs Dogs Classifier",
        "Models are Trained: Time to Dig Up!",
        "DVC + Streamlit = ❤️",
        "Conclusion",
    ],
    paths=[
        "pages/introduction.py",
        "pages/dvc_training_pipeline.py",
        "pages/dig_with_streamlit.py",
        "pages/dvc_and_streamlit.py",
        "pages/conclusion.py",
    ],
    icons=[],  # from https://icons.getbootstrap.com/
    save_answers=False,
    orientation="vertical",
)
