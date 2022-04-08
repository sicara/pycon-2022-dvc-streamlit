import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import make_img, st_write_bs4

st.title("Help me DVC, you are my only hope!")

col_intro_a, col_intro_b, col_intro_c = st.columns([3, 3, 2])

with col_intro_a:
    st.image(str(IMAGES_DIR / "dvc-logo.png"), use_column_width=True)

with col_intro_b:
    st.markdown(
        """
- DVC = **D**ata **V**ersion **C**ontrol
- open source library
- 9.5k ⭐ on Github
- written in Python
- made by iterative.ai
    """
    )


with col_intro_c:
    st.image(str(IMAGES_DIR / "tweet-dvc-love.png"), use_column_width=True)


col_a, col_b = st.columns([2, 3])

with col_a:
    st.write("### 🔗 Version the data")
    st.markdown(
        """
- replaces large files with small metafiles easy to handle with Git
- has a similar command line interface: `dvc add/checkout`
    """
    )

    st.write("### 🤝 Remote storage for sharing")
    st.markdown(
        """
- agnostic to storage, on-premise or cloud
- has a similar command line interface: `dvc pull/push`
    """
    )

with col_b:
    # Jump line
    st.write("")
    st.write("")
    st_write_bs4(make_img(src=IMAGES_DIR / "dvc-core-principle.svg"))
