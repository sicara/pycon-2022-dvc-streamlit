import streamlit as st

st.title("Run an Experiment, Second Try")

col_a, col_b = st.columns(2)

with col_a:
    st.write("### 1️⃣ Setup the experiment")
    st.markdown(
        """
- modify data, script just like before
- modify the pipeline: `dvc.yaml`
- modify the parameters: `parameters.yaml`
"""
    )
    st.write("### 😀")

with col_b:
    st.write("### 2️⃣ Run the pipeline")
    st.write("- Just run `dvc repro dvc.yaml`")
    st.write("### 😀")

col_c, col_d = st.columns(2)

with col_c:
    st.write("### 3️⃣ Save the results")
    st.markdown(
        """
- output data is saved in the dvc (local) cache
- just run `dvc push` to upload to the remote storage
    """
    )
    st.write("### 😀")

with col_d:
    st.write("### 4️⃣ Put the experiment in the right place")
    st.markdown(
        """
Save the metadata (experiment name, used parameters, commit hash, link to output files):
- in the git commit history: `git log`
"""
    )
    st.write("### 😑")
