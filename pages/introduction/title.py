import streamlit as st

from constants import TITLE
from utils.html_factory import CSSStyle, make_div, st_write_bf4

big_title_style = CSSStyle(
    text_align="center",
    font_size="58px",
    margin="80px 150px 80px 150px",
    font_weight="bold",
)
big_title = make_div(style=big_title_style, text=TITLE)

st_write_bf4(big_title)
