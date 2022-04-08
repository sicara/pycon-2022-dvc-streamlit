import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import CSSStyle, make_img, st_write_bs4

st.title("R&D is a non linear workflow")

schema_style = CSSStyle(width="80%", margin="0 auto", display="block")

st.write("### 🧑‍💻 Classical software development is (mostly) a linear workflow:")
st_write_bs4(make_img(src=IMAGES_DIR / "software_engineering_is_linear_workflow.svg", style=schema_style))

st.write("### 🧪 Data Science is not:")
st_write_bs4(make_img(src=IMAGES_DIR / "randd_is_non_linear_workflow.svg", style=schema_style))
