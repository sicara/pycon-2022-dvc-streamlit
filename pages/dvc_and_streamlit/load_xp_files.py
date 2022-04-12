import dvc.api
import dvc.repo
import pandas as pd
import streamlit as st

from constants import CODE_DIR, ROOT_DIR

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


def load_predictions(rev: str) -> pd.DataFrame:
    with dvc.api.open(EVALUATION_DIR / "predictions.csv", rev=rev) as file:
        return pd.read_csv(file)


st.write("2️⃣ Feed it with experiment commits:")
st.code(
    """
experiments_options = [{
        "name": experiment_metadata["data"].get("name", "-"),
        "commit": experiment_commit_sha[:6],
    }
    for commit_parent_sha, experiments in experiments_metadata.items()
    for experiment_commit_sha, experiment_metadata in experiments.items()
]

selected_rev = st.selectbox(
    label="Select an experiment",
    options=experiments_options,
    format_func=lambda xp: f"{xp['commit']} ({xp['name']})",
)
"""
)

DVC_REPO = dvc.repo.Repo(".")

experiment_commits = DVC_REPO.experiments.ls(all_=True)
experiments_metadata = DVC_REPO.experiments.show(revs=list(experiment_commits))

experiments_options = [
    {
        "name": experiment_metadata["data"].get("name", "-"),
        "commit": experiment_commit_sha,
    }
    for commit_parent_sha, experiments in experiments_metadata.items()
    for experiment_commit_sha, experiment_metadata in experiments.items()
    if experiment_commit_sha != "baseline"
]


selected_rev = st.selectbox(
    label="Select an experiment",
    options=experiments_options,
    format_func=lambda xp: f"{xp['commit']} ({xp['name']})",
)
