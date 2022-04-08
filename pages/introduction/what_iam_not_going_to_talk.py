import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import make_img, st_write_bs4

st.title("What I am not going to talk about today")

st_write_bs4(make_img(src=IMAGES_DIR / "off-the-shelves-monolithic-ai-platforms.svg"))
