import streamlit as st

st.title("Interactive UI for Metrics")


def get_code_dynamic_metrics():
    CODE_FILEPATH = "code_samples/dynamic_metrics.py"

    with open(CODE_FILEPATH, "r") as f:
        initial_code = f.read()

    return initial_code


col_a, col_b = st.columns(2)

st_code = get_code_dynamic_metrics()

with col_a:
    st.write("### 🧑‍💻 In the code")
    st.code(st_code)

with col_b:
    st.write("### 🚀 In Streamlit")
    try:
        exec(st_code)
    except Exception as e:
        st.error(f"Error: {e}")
