import streamlit as st

st.title("Machine Learning Engineers are Software Engineers !")

col_a, col_b = st.columns(2)

with col_a:
    st.info(
        """
### Leverage best practices and best tools for coding

- Do not reinvent the wheel!
- ...
"""
    )

with col_b:
    st.success(
        """
### Introduce ML-specific tools only when it is really needed

- ...
- Experiment tracking !
"""
    )
