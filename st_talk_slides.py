import streamlit as st
import streamlit_book as stb

import constants

# Streamlit webpage properties
st.set_page_config(
    page_title=constants.CONFERENCE_NAME,
    page_icon=str(constants.CONFERENCE_LOGO_PATH),
    layout="wide",
)

conf_column_logo, conf_column_name = st.sidebar.columns([1, 3])
with conf_column_logo:
    st.image(str(constants.CONFERENCE_LOGO_PATH), width=55)
with conf_column_name:
    st.write(
        f"""
<div style="text-align: left; font-size: 18px; margin-top: -10px; font-weight: bold">
    {constants.CONFERENCE_NAME}
</div>
<div style="text-align: left; font-size: 14px">
    {constants.CONFERENCE_DATE}
</div>
<div style="text-align: left; font-size: 14px; margin-bottom: 10px; font-style: italic">
    {constants.AUTHOR}
</div>
    """,
        unsafe_allow_html=True,
    )


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
