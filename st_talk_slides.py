import streamlit as st

import constants
from pages import conclusion, dig_with_streamlit, dvc_and_streamlit, dvc_training_pipeline, introduction
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4
from utils.title import st_write_title

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
sidebar_header = make_div(style=CSSStyle(margin_top="-40px", margin_bottom="20px", display="flex"))
sidebar_header.extend([sidebar_header_logo, sidebar_header_title])


with st.sidebar:
    st_write_bs4(sidebar_header)

# Main Chapter selection
NO_CHAPTER = "👋 Hello :)"

selected_part = st.sidebar.selectbox(
    label="📚 Today's menu:",
    options=[NO_CHAPTER, *constants.CHAPTERS],
)

# Show chapters
if selected_part == NO_CHAPTER:
    st_write_title()
elif selected_part == constants.CHAPTER_INTRODUCTION:
    introduction.st_show()
elif selected_part == constants.CHAPTER_ML_PIPELINE:
    dvc_training_pipeline.st_show()
elif selected_part == constants.CHAPTER_ML_ANALYSIS:
    dig_with_streamlit.st_show()
elif selected_part == constants.CHAPTER_DVC_AND_STREAMLIT:
    dvc_and_streamlit.st_show()
elif selected_part == constants.CHAPTER_CONCLUSION:
    conclusion.st_show()
else:
    st.error("Unknown chapter")
