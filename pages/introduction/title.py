import streamlit as st

from constants import TITLE

st.write(
    f"""<div style="text-align: center; font-size: 48px; margin-top: 80px; font-weight: bold">
{TITLE}
</div>""",
    unsafe_allow_html=True,
)
