import streamlit as st

from constants import IMAGES_DIR

st.title("Inception")

st.write("### 🌀 The slides that talk about Streamlit are made with Streamlit")

col_intro_a, col_intro_b = st.columns([2, 3])

with col_intro_a:
    st.image(str(IMAGES_DIR / "streamlit-logo.png"), use_column_width=True)

    st.markdown(
        """
- open source library
- 18.6k ⭐ on Github
- written in Python and Javascript (ReactJS)
- now part of Snowflake (March 22)
- awesome community developing tons of custom components
- thanks @sebastiandres for `streamlit_book` :)
    """
    )

with col_intro_b:
    st.write("(Soon) the Most popular library for building data dashboard in Python:")
    st.image(str(IMAGES_DIR / "streamlit-star-history.png"), use_column_width=True)
