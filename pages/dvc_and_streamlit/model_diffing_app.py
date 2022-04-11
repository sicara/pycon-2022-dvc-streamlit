import streamlit as st

st.title("Comparing two models")


def get_code_model_diffing():
    CODE_FILEPATH = "code_samples/diffing_models.py"

    with open(CODE_FILEPATH, "r") as f:
        initial_code = f.read()

    return initial_code


st_code = get_code_model_diffing()

st.write("### 🧑‍💻 In the code")
st.code(st_code)

st.write("### 🚀 In Streamlit")
try:
    exec(st_code)
except Exception as e:
    st.error(f"Error: {e}")
