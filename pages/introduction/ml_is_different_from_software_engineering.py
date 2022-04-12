import streamlit as st

from constants import IMAGES_DIR

st.title("ML Engineering is more than Software Engineering")

_, fig_col, _ = st.columns([1, 5, 1])

fig_col.image(
    str(IMAGES_DIR / "hidden-tech-debt.png"),
    use_column_width=True,
    caption="Hidden Technical Debt in Machine Learning Systems, Sculley et Al, Neurips 2015",
)

# Jump lines
st.write("")
st.write("")

_, icon_col_a, _, icon_col_b, _, icon_col_c, _ = st.columns([3, 4, 4, 4, 4, 4, 3])

with icon_col_a:
    st.image(str(IMAGES_DIR / "data-icon.png"), use_column_width=True)

with icon_col_b:
    st.image(str(IMAGES_DIR / "exploration-icon.png"), use_column_width=True)

with icon_col_c:
    st.image(str(IMAGES_DIR / "investigate-icon.png"), use_column_width=True)


_, text_col_a, _, text_col_b, _, text_col_c, _ = st.columns([1, 3, 1, 3, 1, 3, 1])

with text_col_a:
    st.write("Need to track the data alongside the code")

with text_col_b:
    st.write("Exploratory work, Linear flows do not work")

with text_col_c:
    st.write("Need tools for investigation")
