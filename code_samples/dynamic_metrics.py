import pandas as pd
import streamlit as st

from constants import CODE_DIR

DATA_DIR = CODE_DIR / "data"
EVAL_DIR = DATA_DIR / "evaluation"

preds_df = pd.read_csv(EVAL_DIR / "predictions.csv")
st.dataframe(preds_df.head(3))

threshold = st.slider("Threshold", 0.0, 1.0, 0.5)

preds_df = preds_df.assign(
    predicted_with_threshold=(
        pd.Series("cats", index=preds_df.index)
        .mask(preds_df.prediction > threshold, "dogs")
    )
)
st.dataframe(preds_df.head(3))

accuracy = (
    preds_df.true_label == preds_df.predicted_with_threshold
).mean()

st.metric(label="Accuracy", value=accuracy)
