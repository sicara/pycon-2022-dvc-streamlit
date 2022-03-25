import streamlit as st

import constants
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4

# Title
big_title_style = CSSStyle(
    text_align="center",
    font_size="64px",
    line_height="64px",
    margin="40px 80px 60px 80px",
    font_weight=700,
)
big_title = make_div(style=big_title_style, text=constants.TITLE)

st_write_bs4(big_title)


# Author
author_style = CSSStyle(
    text_align="center",
    font_size="48px",
    line_height="48px",
    font_style="italic",
    margin_bottom="40px",
)
author = make_div(style=author_style, text=constants.AUTHOR)

st_write_bs4(author)


# Conference
st_write_bs4(
    make_img(
        style=CSSStyle(
            text_align="center",
            width="80%",
            margin_left="auto",
            margin_right="auto",
            display="block",
        ),
        src=constants.CONFERENCE_FULL_LOGO_PATH,
    ),
)
