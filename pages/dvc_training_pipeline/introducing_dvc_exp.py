import streamlit as st

from constants import IMAGES_DIR
from utils.html_factory import make_img, st_write_bs4

st.title("🧪 DVC Experiments")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown(
        """
### 🔩 How does it work?
It relies on git custom references:
- a git reference is simply a commit name:
  - branches refs in `.git/refs/heads/`
  - tags refs in `.git/refs/tags/`
  - handled using high-level git **"porcelain"** commands: `git branch` or `git tag`
- experiment commits are tracked by special refs:
  - located in `.git/refs/exps/`
  - DVC handles them using lower-level git **"plumbing"** commands
    """
    )


with col_b:
    st.write("### 🚀 The `dvc exp run` command:")
    st.code("dvc exp run dvc.yaml --set-params train.seed=1234", language="bash")
    st.markdown(
        """
1. edit the `parameters.yaml` file accordingly to the `-set-params` options
2. run the `dvc.yaml` pipeline just like `dvc repro`
3. create a commit and track it with a git custom reference

Experiments can be queued using `--queue` option and run (in parallel) using `--run-all` option.
    """
    )

st_write_bs4(make_img(src=IMAGES_DIR / "git-custom-refs.svg"))
