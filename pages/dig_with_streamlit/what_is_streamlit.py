import streamlit.components.v1 as components

import constants

# TODO: change theme ? Darkmode and streamlit page are not visually compatible
components.iframe(
    "https://streamlit.io/", height=constants.FULL_HEIGHT_PIXELS, scrolling=True
)
