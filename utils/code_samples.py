from pathlib import Path
from typing import Optional

import streamlit as st


def st_write_code_from_file(code_filepath: Path, expanded: Optional[bool] = True, *args, **kwargs) -> None:
    with st.expander(label=f"📄 {code_filepath.name}", expanded=expanded):
        with open(code_filepath, "r") as f:
            st.code(f.read(), *args, **kwargs)
