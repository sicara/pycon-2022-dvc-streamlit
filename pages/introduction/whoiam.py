import streamlit as st

from constants import AUTHOR, IMAGES_DIR
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4

col_a, _, col_b = st.columns([5, 1, 5])

with col_a:
    st.markdown("## Who am I?")
    st.write(f"My name is {AUTHOR}")
    st.write("French, 🇫🇷 🥖")
    st.write("34 years old, father of two daughters 👭")

    TWITTER = make_div()
    TWITTER.extend(
        [
            make_img(src=IMAGES_DIR / "twitter-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
            make_div(text="@AntoineToubhans", style=CSSStyle(display="inline")),
        ]
    )
    st_write_bs4(TWITTER)

    LINKEDIN = make_div()
    LINKEDIN.extend(
        [
            make_img(src=IMAGES_DIR / "linkedin-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
            make_div(text="/antoine-toubhans", style=CSSStyle(display="inline")),
        ]
    )
    st_write_bs4(LINKEDIN)

    GITHUB = make_div()
    GITHUB.extend(
        [
            make_img(src=IMAGES_DIR / "github-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
            make_div(text="/AntoineToubhans", style=CSSStyle(display="inline")),
        ]
    )
    st_write_bs4(GITHUB)

with col_b:
    ME_IMG = make_img(
        src=IMAGES_DIR / "moi.jpeg",
        style=CSSStyle(
            width="50%",
            border_radius="50%",
            margin_bottom="40px",
        ),
    )
    st_write_bs4(ME_IMG)

col_c, _, col_d = st.columns([5, 1, 5])

with col_c:
    st.markdown("### Where do I work?")
    st.write("in Paris, at")
    st.image(str(IMAGES_DIR / "sicara-logo.png"), width=200)

with col_d:
    st.markdown("### Short curriculum")
    st.write("- 🔬 PhD candidate in Computer Science till 2015")
    st.write("- 👨‍💻 Web Developer in 2016")
    st.write("- 🧪 Data Scientist since 2017")
    st.write("- 🧪🧪 Head of Science at Sicara since 2018")
    st.write("- 👁 Work mostly on Computer Vision")
