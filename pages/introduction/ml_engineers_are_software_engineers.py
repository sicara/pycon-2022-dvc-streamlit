import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

df = pd.read_csv(
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv"
)
grid_options = {
    "columnDefs": [
        {
            "headerName": "airline",
            "field": "airline",
            "editable": True,
        },
    ],
}

resp = AgGrid(df, editable=True)  # , grid_options)

st.write(resp["data"])
