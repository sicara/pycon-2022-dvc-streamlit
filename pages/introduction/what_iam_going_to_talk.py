import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import make_img, st_write_bs4

st.title("What I am going to show you today")

st_write_bs4(make_img(src=IMAGES_DIR / "dvc-and-streamlit-approach.svg"))

st.write("### Another approach: build an entire experiment tracking system with small bricks")
