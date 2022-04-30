import streamlit as st

st.title("Comparing Two Models")


def get_code_model_diffing():
    CODE_FILEPATH = "code_samples/diffing_models.py"

    with open(CODE_FILEPATH, "r") as f:
        initial_code = f.read()

    return initial_code


st_code = get_code_model_diffing()

try:
    exec(st_code)
except Exception as e:
    st.error(f"Error: {e}")


with st.expander("🔎 Code"):
    st.code(st_code)
