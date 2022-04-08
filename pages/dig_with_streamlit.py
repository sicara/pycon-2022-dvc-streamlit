import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Dig with Streamlit",
        menu_icon="book",
        options=[
            "What is Streamlit?",
            "Quick demo !",
        ],
        paths=[
            "pages/dig_with_streamlit/what_is_streamlit.py",
            "pages/dig_with_streamlit/streamlit_demo.py",
        ],
        icons=["question", "star"],
        save_answers=False,
        orientation="vertical",
    )
