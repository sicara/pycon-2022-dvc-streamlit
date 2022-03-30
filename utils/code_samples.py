from pathlib import Path

import streamlit as st


def st_write_code_from_file(code_filepath: Path, *args, **kwargs) -> None:
    with st.expander(label=f"📄 {code_filepath.name}", expanded=True):
        with open(code_filepath, "r") as f:
            st.code(f.read(), *args, **kwargs)
