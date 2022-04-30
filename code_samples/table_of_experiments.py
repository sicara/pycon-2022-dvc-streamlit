import dvc.repo
import pandas as pd
import plotly.express as px
import streamlit
import streamlit as st
from st_aggrid import AgGrid, DataReturnMode, GridOptionsBuilder, GridUpdateMode

from constants import ROOT_DIR

DVC_REPO = dvc.repo.Repo(ROOT_DIR)

experiment_commits = DVC_REPO.experiments.ls(all_commits=True)
experiments_metadata = DVC_REPO.experiments.show(revs=list(experiment_commits))

experiments_dict = [
    {
        "name": experiment_metadata["data"]["name"],
        "parent_commit": commit_parent_sha[:6],
        "commit": experiment_commit_sha[:6],
        "date": experiment_metadata["data"]["timestamp"],
        # Parse metrics
        "accuracy": 100 * experiment_metadata["data"]["metrics"]["src/data/evaluation/metrics.json"]["data"]["accuracy"],
        # Parse train parameters
        "batch_size": experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["batch_size"],
        "epochs_frozen": experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["epochs"]["frozen"],
        "epochs_unfrozen": experiment_metadata["data"]["params"]["src/params.yaml"]["data"]["train"]["epochs"]["unfrozen"],
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
gb = GridOptionsBuilder.from_dataframe(experiments_df)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_column("accuracy", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], precision=2)

grid_response = AgGrid(
    experiments_df,
    gridOptions=gb.build(),
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    update_mode=GridUpdateMode.MODEL_CHANGED,
)

selected_experiments_df = experiments_df.loc[experiments_df.name.isin([
    row["name"] for row in grid_response["selected_rows"]
])] if len(grid_response["selected_rows"]) > 0 else experiments_df


st.write("### 📊 Plot bar chart")
selected_col = st.selectbox("Select a column", list(selected_experiments_df.columns), index=4)
streamlit.bar_chart(data=selected_experiments_df.set_index("name")[selected_col])


st.write("### 📈 Scatter Plots")
col_x, col_y, col_l = st.columns(3)
selected_col_x = col_x.selectbox("X axis", list(selected_experiments_df.columns), index=7)
selected_col_y = col_y.selectbox("Y axis", list(selected_experiments_df.columns), index=4)
selected_col_l = col_l.selectbox("Legend", list(selected_experiments_df.columns), index=10)

fig = px.scatter(
    selected_experiments_df.assign(seed=selected_experiments_df.seed.astype(str)),
    y=selected_col_y,
    x=selected_col_x,
    color=selected_col_l,
    symbol=selected_col_l,
)
fig.update_traces(marker_size=10)
st.plotly_chart(fig)
