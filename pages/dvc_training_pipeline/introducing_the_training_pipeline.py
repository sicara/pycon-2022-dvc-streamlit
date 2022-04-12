import streamlit as st

from constants import CODE_DIR, IMAGES_DIR, PARAMS_PATH, PIPELINE_PATH
from utils.code_samples import st_write_code_from_file
from utils.html_factory import CSSStyle, make_img, st_write_bs4

st.title("The Training Pipeline")

script_col, pipeline_col = st.columns([2, 1])

with script_col:
    with st.expander(label="💻 Download dataset", expanded=False):
        st.code(
            """
wget https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip -O cats_and_dogs_filtered.zip
unzip cats_and_dogs_filtered.zip -d data/raw
rm cats_and_dogs_filtered.zip
    """,
            language="bash",
        )

    st_write_code_from_file(code_filepath=CODE_DIR / "scripts" / "split_dataset.py", language="python", expanded=False)
    st_write_code_from_file(code_filepath=CODE_DIR / "scripts" / "train.py", language="python", expanded=False)
    st_write_code_from_file(code_filepath=CODE_DIR / "scripts" / "evaluate.py", language="python", expanded=False)

    st.write("🚀 **Added pipeline and parameters path:**")
    st_write_code_from_file(code_filepath=PIPELINE_PATH, language="yaml", expanded=False)
    st_write_code_from_file(code_filepath=PARAMS_PATH, language="yaml", expanded=False)

with pipeline_col:
    st_write_bs4(make_img(src=IMAGES_DIR / "training-pipeline.svg", style=CSSStyle(position="fixed", width="27%")))
