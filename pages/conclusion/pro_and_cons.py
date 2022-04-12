import streamlit as st

st.write("## Pros and Cons of the DVC+Streamlit Approach")

pros_col, cons_col = st.columns(2)

with pros_col:
    st.markdown(
        """
### 👍
- Evolution of the UI:
  - evolves with the project
  - lead time from an idea popping in mind and make it real
- No limit to UI customization:
  - any media: audio / video / NLP / ...
  - Streamlit custom component in ReactJs
"""
    )


with cons_col:
    st.markdown(
        """
### 👎
- requires **software engineering** skills
- harder to maintain in the long term:
  - retro compatibility as the pipeline evolves
  - technical debt to be handled
"""
    )


# Jump lines
st.write("")
st.write("")
st.write("")

st.markdown(
    """
### 🚀 Next steps
- dealing with the infra (outside the scope of ML experiment tracking)
  - running pipelines on kubernetes
  - run DVC pipeline on any **execution engine**
- integration with CI/CD
  - CML (Continuous Machine Learning) by iterative.ai
"""
)
