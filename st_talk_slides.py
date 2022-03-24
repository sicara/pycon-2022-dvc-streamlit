import streamlit as st
import streamlit_book as stb
from bs4 import BeautifulSoup

import constants
from utils.html_factory import CSSStyle, make_div, st_write_bf4

# Streamlit webpage properties
st.set_page_config(
    page_title=constants.CONFERENCE_NAME,
    page_icon=str(constants.CONFERENCE_LOGO_PATH),
    layout="wide",
)

sidebar_header = BeautifulSoup()
sidebar_header.extend(
    [
        make_div(
            style=CSSStyle(
                text_align="left",
                font_size="18px",
                font_weight="bold",
                margin_top="-10px",
            ),
            text=constants.CONFERENCE_NAME,
        ),
        make_div(
            style=CSSStyle(text_align="left", font_size="14px"),
            text=constants.CONFERENCE_DATE,
        ),
        make_div(
            style=CSSStyle(
                text_align="left",
                font_size="14px",
                font_style="italic",
                margin_bottom="10px",
            ),
            text=constants.AUTHOR,
        ),
    ]
)


conf_column_logo, conf_column_name = st.sidebar.columns([1, 3])
with conf_column_logo:
    st.image(str(constants.CONFERENCE_LOGO_PATH), width=55)
with conf_column_name:
    st_write_bf4(sidebar_header)


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
