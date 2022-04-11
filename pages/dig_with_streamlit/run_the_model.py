import streamlit as st

st.title("Run the model")


def get_code_run_the_model():
    CODE_FILEPATH = "code_samples/run_the_model.py"

    with open(CODE_FILEPATH, "r") as f:
        initial_code = f.read()

    return initial_code


col_a, col_b = st.columns(2)

st_code = get_code_run_the_model()

with col_a:
    st.write("### 🧑‍💻 In the code")
    st.code(st_code)

with col_b:
    st.write("### 🚀 In Streamlit")
    try:
        exec(st_code)
    except Exception as e:
        st.error(f"Error: {e}")
