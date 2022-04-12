import streamlit as st

from utils.commands import st_command

st.title("🧪 See the Experiment Table")

st.write("### 🚀 Cheat sheet")
col_a, col_b = st.columns(2)
with col_a:
    st.write("See experiments from all commits:")
    st.code("dvc exp show --all-commit", language="bash")

    st.write("See experiments deriving from a commit:")
    st.code("dvc exp show --rev COMMIT_SHA", language="bash")

with col_b:
    st.write("Select columns to display:")
    st.code("dvc exp show --drop [\s\S]* --keep Experiment|accuracy|train.seed|train.fine_tune_at", language="bash")

    st.write("Sort experiments:")
    st.code("dvc exp show --sort-by COLUMN --sort-order {asc|desc}", language="bash")


st_command(label='Try the "dvc exp show" command:', initial_command="dvc exp show --all-commits")
