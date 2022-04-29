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
sidebar_header = make_img(
    src=constants.IMAGES_DIR / "pycon_2022.svg",
    style=CSSStyle(
        width="70%",
        margin="-60px 0 5px 0",
        display="block",
    ),
)

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
