import streamlit_book as stb

# Streamlit book properties
stb.set_book_config(
    menu_title="Dig with Streamlit",
    menu_icon="book",
    options=[
        "What is Streamlit?",
    ],
    paths=[
        "pages/dig_with_streamlit/what_is_streamlit.py",
    ],
    save_answers=False,
    orientation="vertical",
)
