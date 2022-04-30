import streamlit as st

from constants import CODE_DIR

EVALUATION_DIR = CODE_DIR / "data" / "evaluation"

st.title("Load Files from Anywhere")

st.markdown(
    """
- useful to compare two models tracked by different commits
- use `dvc.api.open()` from the DVC python API: like regular `open()` but open to a new dimension :)
"""
)

st.write("1️⃣ A function to load predictions from any commit:")

st.code(
    """
def load_predictions(rev: str) -> pd.DataFrame:
    with dvc.api.open(EVALUATION_DIR / "predictions.csv", rev=rev) as file:
        return pd.read_csv(file)
""",
    language="python",
)

st.write("2️⃣ Feed it with experiment commits:")
st.code(
    """
selected_rev = st.selectbox(
    label="Select an experiment",
    options=experiments_options,
    format_func=lambda xp: f"{xp['commit']} ({xp['name']})",
)

predictions = load_predictions(rev=selected_rev["commit"])
"""
)
