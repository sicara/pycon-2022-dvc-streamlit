import streamlit as st

from constants import PARAMS_PATH, PIPELINE_PATH
from utils.code_samples import st_write_code_from_file

col_a, col_b = st.columns(2)

with col_a:
    st_write_code_from_file(code_filepath=PIPELINE_PATH, language="yaml")

with col_b:
    st_write_code_from_file(code_filepath=PARAMS_PATH, language="yaml")
