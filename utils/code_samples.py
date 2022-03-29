import streamlit as st


def st_write_code_sample(code_sample_file: str) -> None:
    from constants import CODE_SAMPLES_DIR

    st.write(CODE_SAMPLES_DIR)
    with open(CODE_SAMPLES_DIR / code_sample_file, "r") as f:
        st.code(f.read())
