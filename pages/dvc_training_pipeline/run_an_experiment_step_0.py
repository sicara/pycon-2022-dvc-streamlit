import streamlit as st

st.title("Run an experiment, first try")

col_a, col_b = st.columns(2)

with col_a:
    st.write("### 1️⃣ Setup the experiment")
    st.markdown(
        """
- modify the data: splits, preprocessing, ...
- modify the model: architecture, hyperparameters, ...
- modify the scripts themselves"
"""
    )
    st.write("### 😀")

with col_b:
    st.write("### 2️⃣ Run the pipeline")
    st.write("- Run the scripts, in the right order !")
    st.code(
        """
wget ...
python split_dataset.py
python train.py
python evaluate.py
""",
        language="bash",
    )
    st.write("### 😑")

col_c, col_d = st.columns(2)

with col_c:
    st.write("### 3️⃣ Save the results")
    st.markdown(
        """
    Save the output data (dataset, NN weights, metrics) **somewhere**:
    - a bucket
    - a drive
    - your laptop hard drive
    - ?
    """
    )
    st.write("### 😶")

with col_d:
    st.write("### 4️⃣ Put the experiment in the right place")
    st.markdown(
        """
Save the metadata (experiment name, used parameters, commit hash, link to output files) **somewhere**:
- a note on your laptop
- a shared spreadsheet
- ?
"""
    )
    st.write("### 😰")
