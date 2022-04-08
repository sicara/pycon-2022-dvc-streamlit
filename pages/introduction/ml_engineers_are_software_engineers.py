import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import CSSStyle, make_img, st_write_bs4

st.title("What is Machine Learning Engineering?")

st.markdown("It is a cross-field job:")

st_write_bs4(
    make_img(
        IMAGES_DIR / "ml_engineer_is_software_engineer.svg",
        style=CSSStyle(width="80%", margin="30px auto", display="block"),
    )
)


st.write("### Leverage best practices and best tools for coding: do not reinvent the wheel!")
