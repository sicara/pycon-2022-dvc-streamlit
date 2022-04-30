import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import make_img, st_write_bs4

st.title("Help me DVC, you are my only hope!")

_, logo_col, _ = st.columns([3, 2, 3])
logo_col.image(str(IMAGES_DIR / "dvc-logo.png"), use_column_width=True)


col_a, col_b = st.columns(2)

with col_a:
    st.write("### 🔗 Version the data")
    st.markdown(
        """
- replaces large files with small metafiles easy to handle with Git
- has a similar command line interface: `dvc add/checkout`
    """
    )

with col_b:
    st.write("### 🤝 Remote storage for sharing")
    st.markdown(
        """
- agnostic to storage, on-premise or cloud
- has a similar command line interface: `dvc pull/push`
    """
    )

st_write_bs4(make_img(src=IMAGES_DIR / "dvc-core-principle.svg"))
