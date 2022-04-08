import streamlit as st

st.title("Run an experiment, third try")

col_a, col_b = st.columns(2)

with col_a:
    st.write("### 1️⃣ Setup the experiment")
    st.markdown(
        """
- modify data, script or pipeline just like before
- put experiments in the queue:
  - `dvc exp run --set-params train.seed=1234 --queue`
  - `dvc exp run --set-params train.seed=9876 --queue`
  - ...
"""
    )
    st.write("### 😀😀")

with col_b:
    st.write("### 2️⃣ Run the pipeline")
    st.write("- Just run `dvc exp run --run-all`")
    st.write("- run in parallel")
    st.write("### 😀")

col_c, col_d = st.columns(2)

with col_c:
    st.write("### 3️⃣ Save the results")
    st.markdown(
        """
- output data is saved in the dvc (local) cache
- run `dvc exp push`:
  - upload data to the remote storage
  - ⚠️ push git custom refs to git remote server
    """
    )
    st.write("### 😀")

with col_d:
    st.write("### 4️⃣ Put the experiment in the right place")
    st.markdown(
        """
Save the metadata (experiment name, used parameters, commit hash, link to output files):
- in the experiment table: `dvc exp show`
"""
    )
    st.write("### 😀")
