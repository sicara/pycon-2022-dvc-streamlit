import dvc.repo
import pandas as pd
import plotly.express as px
import streamlit
import streamlit as st
from st_aggrid import AgGrid

from constants import ROOT_DIR

DVC_REPO = dvc.repo.Repo(ROOT_DIR)

experiment_commits = DVC_REPO.experiments.ls(all_=True)
experiments_metadata = DVC_REPO.experiments.show(revs=list(experiment_commits))

experiments_dict = [
    {
        "name": experiment_metadata["data"]["name"],
        "parent_commit": commit_parent_sha[:6],
        "commit": experiment_commit_sha[:6],
        # Parse metrics
        "accuracy": experiment_metadata["data"]["metrics"]["src/data/evaluation/metrics.json"]["data"]["accuracy"],
        # Parse train parameters
        "batch_size": experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["batch_size"],
        "epochs": sum(
            experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["epochs"].values()
        ),
        "fine_tune_at": experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["fine_tune_at"],
        "learning_rate": experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["learning_rate"],
        "seed": experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["seed"],
    }
    for commit_parent_sha, experiments in experiments_metadata.items()
    if commit_parent_sha != "workspace"
    for experiment_commit_sha, experiment_metadata in experiments.items()
    if experiment_commit_sha != "baseline"
]

experiments_df = pd.DataFrame(experiments_dict)

AgGrid(experiments_df)

st.write("Experiment Accuracies:")
streamlit.bar_chart(data=experiments_df.set_index("name").accuracy)


st.write("Accuracy vs. Fine Tune At:")
fig = px.scatter(
    experiments_df.assign(seed=experiments_df.seed.astype(str)),
    y="fine_tune_at",
    x="accuracy",
    color="seed",
    symbol="seed",
)
fig.update_traces(marker_size=10)
st.plotly_chart(fig)
