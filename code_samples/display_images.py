import pandas as pd
import streamlit as st

from constants import CODE_DIR

DATA_DIR = CODE_DIR / "data"
EVAL_DIR = DATA_DIR / "evaluation"

preds_df = pd.read_csv(EVAL_DIR / "predictions.csv")

min_threshold, max_threshold = st.slider(
    label="Threshold",
    min_value=0.0,
    max_value=1.0,
    value=(0.1, 0.9),
)

unsure_preds_df = preds_df.loc[
    (preds_df.prediction >= min_threshold)
    & (preds_df.prediction <= max_threshold)
]
st.write(f"Unsure predictions: {len(unsure_preds_df)}")

st.image(
    unsure_preds_df.head(4).image_path.to_list(),
    width=150,
)
