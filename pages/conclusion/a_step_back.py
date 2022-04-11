import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import CSSStyle, make_img, st_write_bs4

st.title("ML Experiment Tracking System")
st.write("Let's take a (final) step back:")

st_write_bs4(
    make_img(
        IMAGES_DIR / "step-back-post-streamlit.svg",
        style=CSSStyle(width="100%"),
    )
)
