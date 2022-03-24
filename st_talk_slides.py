import streamlit as st
import streamlit_book as stb

import constants
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4

# Streamlit webpage properties
st.set_page_config(
    page_title=constants.CONFERENCE_NAME,
    page_icon=str(constants.CONFERENCE_LOGO_PATH),
    layout="wide",
)

# Sidebar Header
sidebar_header_logo = make_img(
    src=constants.CONFERENCE_LOGO_PATH,
    style=CSSStyle(width="64px", flex=1, margin_right="20px"),
)
sidebar_header_title = make_div(style=CSSStyle(text_align="left", flex=3))
sidebar_header_title.extend(
    [
        make_div(
            style=CSSStyle(font_size="18px", font_weight="bold"),
            text=constants.CONFERENCE_NAME,
        ),
        make_div(
            style=CSSStyle(font_size="14px"),
            text=constants.CONFERENCE_DATE,
        ),
        make_div(
            style=CSSStyle(font_size="14px", font_style="italic"),
            text=constants.AUTHOR,
        ),
    ]
)
sidebar_header = make_div(
    style=CSSStyle(margin_top="-40px", margin_bottom="20px", display="flex")
)
sidebar_header.extend([sidebar_header_logo, sidebar_header_title])


with st.sidebar:
    st_write_bs4(sidebar_header)


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
