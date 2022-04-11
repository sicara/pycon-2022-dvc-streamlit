import streamlit as st

st.title("The Table of Experiments")


def get_code_experiment_tables():
    CODE_FILEPATH = "code_samples/table_of_experiments.py"

    with open(CODE_FILEPATH, "r") as f:
        initial_code = f.read()

    return initial_code


st_code = get_code_experiment_tables()

st.write("### 🧑‍💻 In the code")
st.code(st_code)

st.write("### 🚀 In Streamlit")
try:
    exec(st_code)
except Exception as e:
    st.error(f"Error: {e}")
