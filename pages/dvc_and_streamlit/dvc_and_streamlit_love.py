import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import CSSStyle, make_img, st_write_bs4

st.title("Combine DVC and Streamlit Strengths")

st_write_bs4(
    make_img(
        IMAGES_DIR / "dvc-streamlit-love.svg",
        style=CSSStyle(width="100%"),
    )
)
