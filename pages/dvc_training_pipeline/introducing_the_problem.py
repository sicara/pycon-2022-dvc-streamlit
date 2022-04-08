import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import CSSStyle, make_img, st_write_bs4

st.title("Classify images of cats and dogs")

st.write("Problem adapted from a Tensorflow tutorial: Transfer learning and fine-tuning")

st.image(str(IMAGES_DIR / "tutorial-colab.png"), width=1024)
st_write_bs4(make_img(src=IMAGES_DIR / "cats_or_dog_model.svg", style=CSSStyle(width="80%")))
