import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import CSSStyle, make_img, st_write_bs4

st.title("Why an ML Experiment Tracking System?")

st_write_bs4(
    make_img(
        IMAGES_DIR / "ml_xp_tracking_system_lifecycle.svg",
        style=CSSStyle(width="95%", margin="0 auto", display="block"),
    )
)
