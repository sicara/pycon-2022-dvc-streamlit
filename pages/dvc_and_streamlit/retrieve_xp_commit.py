import dvc.repo
import streamlit as st

from constants import ROOT_DIR

st.title("Retrieving experiments commits")
st.markdown(
    """
- first step to (re)build a table of experiments
- use the DVC internal python API: similar to git python API
"""
)

st.write("1️⃣ Initialize the DVC repo:")

st.code(
    """
import dvc.repo

DVC_REPO = dvc.repo.Repo(".")
""",
    language="python",
)

DVC_REPO = dvc.repo.Repo(ROOT_DIR)

st.write("2️⃣ Retrieve experiments parent commits:")

st.code("experiment_commits = DVC_REPO.experiments.ls(all_=True)", language="python")
experiment_commits = DVC_REPO.experiments.ls(all_=True)
st.write(experiment_commits)

st.write("3️⃣ Retrieve experiments metadata:")
st.code("experiments_metadata = DVC_REPO.experiments.show(revs=list(experiment_commits))", language="python")

experiments_metadata = DVC_REPO.experiments.show(revs=list(experiment_commits))
st.write(experiments_metadata)
