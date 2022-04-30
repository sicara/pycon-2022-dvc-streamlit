import dvc.repo
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from constants import ROOT_DIR

DVC_REPO = dvc.repo.Repo(ROOT_DIR)


@st.experimental_memo
def load_predictions(rev: str) -> pd.DataFrame:
    import dvc.api
    import pandas as pd

    from constants import CODE_DIR

    EVALUATION_DIR = CODE_DIR / "data" / "evaluation"

    with dvc.api.open(str(EVALUATION_DIR / "predictions.csv"), rev=rev) as file:
        return pd.read_csv(file)


experiment_commits = DVC_REPO.experiments.ls(all_commits=True)
experiments_metadata = DVC_REPO.experiments.show(revs=list(experiment_commits))

experiments_options = [
    {
        "name": experiment_metadata["data"].get("name", "-"),
        "commit": experiment_commit_sha[:6],
    }
    for commit_parent_sha, experiments in experiments_metadata.items()
    for experiment_commit_sha, experiment_metadata in experiments.items()
    if experiment_commit_sha != "baseline"
]

fst_xp_column, snd_xp_column = st.columns(2)

with fst_xp_column:
    selected_fst_rev = st.selectbox(
        label="Select first experiment",
        options=experiments_options,
        format_func=lambda xp: f"{xp['commit']} ({xp['name']})",
    )

    fst_predictions = load_predictions(rev=selected_fst_rev["commit"])
    fst_accuracy = (fst_predictions.true_label == fst_predictions.predicted_label).mean()

    st.metric(label="Accuracy", value=f"{100 * fst_accuracy:.2f}%")

with snd_xp_column:
    selected_snd_rev = st.selectbox(
        label="Select second experiment",
        options=experiments_options,
        format_func=lambda xp: f"{xp['commit']} ({xp['name']})",
    )

    snd_predictions = load_predictions(rev=selected_snd_rev["commit"])
    snd_accuracy = (snd_predictions.true_label == snd_predictions.predicted_label).mean()

    st.metric(label="Accuracy", value=f"{100 * snd_accuracy:.2f}%")

merged_predictions = pd.merge(
    left=fst_predictions,
    right=snd_predictions.drop(columns=["image_path", "true_label"]),
    on=["image_name"],
    suffixes=("_fst", "_snd"),
    how="outer",
)

disagree_predictions = merged_predictions.loc[
    merged_predictions["predicted_label_fst"] != merged_predictions["predicted_label_snd"]
]

# Hack to get the image path from the raw image path in tmp xp dir
def fix_image_path(raw_image_path):
    from pathlib import Path

    from constants import CODE_DIR

    image_path = Path(raw_image_path)
    return str(CODE_DIR / image_path.relative_to(image_path.parents[4]))


if disagree_predictions.empty:
    st.write("No disagreements found")
else:
    st.write("Disagreements:")
    AgGrid(disagree_predictions)

    st.image(
        disagree_predictions.image_path.map(fix_image_path).to_list(),
        width=150,
    )
