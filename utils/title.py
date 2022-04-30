import constants
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4

# Title
TITLE_P1 = "Flexible ML Experiment Tracking System"
TITLE_P2 = "for Python Coders"
TITLE_P3 = "with DVC and Streamlit"

BIG_TITLE_STYLE = CSSStyle(
    text_align="center",
    font_size="58px",
    line_height="58px",
    margin="15px 0px 45px 0px",
    font_weight=700,
)
BIG_TITLE_DIV = make_div(style=BIG_TITLE_STYLE)
BIG_TITLE_DIV.extend(
    [
        make_div(text=TITLE_P1),
        make_div(text=TITLE_P2),
        make_div(text=TITLE_P3),
    ]
)


# Conf Logo
BIG_LOGO_STYLE = CSSStyle(
    text_align="center",
    # Ugly CSS that works on my macbook pro and a 133% zoom on chrome
    width="119%",
    margin_left="-80px",
    margin_right="auto",
    display="block",
)

BIG_LOGO_IMG = make_img(
    style=BIG_LOGO_STYLE,
    src=constants.CONFERENCE_FULL_LOGO_PATH,
)


# main
def st_write_title():
    st_write_bs4(BIG_TITLE_DIV)
    st_write_bs4(BIG_LOGO_IMG)
