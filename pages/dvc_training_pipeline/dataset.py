import pandas as pd
import plost
import streamlit as st

from constants import CODE_DIR

st.title("The cats vs. dogs dataset")


def get_image_path(df: pd.DataFrame) -> pd.Series:
    from constants import CODE_DIR

    return (CODE_DIR / "data" / "dataset" / df.split / df.label / df.image_name).astype(str)


dataset = pd.read_csv(CODE_DIR / "data" / "dataset" / "dataset.csv").assign(image_path=get_image_path)

st.write(f"The cats vs. dogs dataset is available in tensorflow_dataset (`tsds`): {len(dataset)} images")


col_a, col_b, col_c = st.columns(3)

col_a.table(
    dataset.pivot_table(index="split", columns="label", values="image_name", aggfunc="count").loc[
        ["train", "val", "test"]
    ]
)
with col_b:
    plost.donut_chart(
        data=dataset.split.value_counts().reset_index(),
        theta="split",
        color="index",
    )
with col_c:
    plost.donut_chart(
        data=dataset.label.value_counts().reset_index(),
        theta="label",
        color="index",
    )

more_cats_and_dogs_clicked = st.button("Get cats and dogs !")

N_CATS_AND_DOGS = 8
col_dogs, col_cats = st.columns(2)

with col_cats:
    some_cats = dataset.loc[lambda df: df.label == "cats"].sample(N_CATS_AND_DOGS)
    st.write("Some cats:")
    st.image([row.image_path for row in some_cats.itertuples()], width=150)

with col_dogs:
    some_dogs = dataset.loc[lambda df: df.label == "dogs"].sample(N_CATS_AND_DOGS)
    st.write("Some dogs:")
    st.image([row.image_path for row in some_dogs.itertuples()], width=150)
