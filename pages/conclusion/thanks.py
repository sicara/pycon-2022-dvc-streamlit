import streamlit as st

from constants import CONFERENCE_FULL_LOGO_PATH, IMAGES_DIR
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4

st.markdown("# Thank you 🙏!")

TWITTER = make_div()
TWITTER.extend(
    [
        make_img(src=IMAGES_DIR / "twitter-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
        make_div(text="@AntoineToubhans", style=CSSStyle(display="inline")),
    ]
)
st_write_bs4(TWITTER)

GITHUB = make_div()
GITHUB.extend(
    [
        make_img(src=IMAGES_DIR / "github-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
        make_div(text="/AntoineToubhans", style=CSSStyle(display="inline")),
    ]
)
st_write_bs4(GITHUB)

st.write("")
st.write("Find the slides and pipeline code: https://github.com/sicara/pycon-2022-dvc-streamlit/tree/pycon-us-2022")


BIG_LOGO_STYLE = CSSStyle(
    text_align="center",
    # Ugly CSS that works on my macbook pro and a 133% zoom on chrome
    width="119%",
    margin_left="-80px",
    margin_right="auto",
    margin_top="70px",
    display="block",
)

BIG_LOGO_IMG = make_img(
    style=BIG_LOGO_STYLE,
    src=CONFERENCE_FULL_LOGO_PATH,
)


st_write_bs4(BIG_LOGO_IMG)
