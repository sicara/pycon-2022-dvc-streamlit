import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import make_img, st_write_bs4

st.title("♻️ DVC Reproducible Pipelines")

col_a, col_b = st.columns([3, 2])

with col_a:
    st.write("📄 Define a pipeline in `dvc.yaml` file:")
    st.code(
        """
stages:
    stage_one:
        cmd: python script_one.py
        deps:
        - file_A
        - file_B
        - script_one.py  # it's a dependency !
        outs:
        - file_D
    stage_two:
        cmd: python script_two.py
        deps:
        - file_C
        - file_D
        - script_two.py  # it's a dependency !
        outs:
        - file_E
    """,
        language="yaml",
    )

    st.write("🚀 Run the pipeline with command `dvc repro dvc.yaml`")
    st.markdown(
        """
- resolves the DAG to execute the stages in the right order
- tracks input/output data with DVC
- restore outputs for cached stages (if dependencies are unchanged)
    """
    )

with col_b:
    st_write_bs4(make_img(src=IMAGES_DIR / "dvc-example-pipeline.svg"))
