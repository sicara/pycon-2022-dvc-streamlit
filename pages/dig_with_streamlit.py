import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Streamlit",
        menu_icon="book",
        options=[
            "What is Streamlit?",
            "Inception",
            "Quick demo!",
            "Make metrics interactive",
            "Display images",
            "Run the model",
        ],
        paths=[
            "pages/dig_with_streamlit/what_is_streamlit.py",
            "pages/dig_with_streamlit/inception.py",
            "pages/dig_with_streamlit/streamlit_demo.py",
            "pages/dig_with_streamlit/dynamic_metrics.py",
            "pages/dig_with_streamlit/display_images.py",
            "pages/dig_with_streamlit/run_the_model.py",
        ],
        icons=["question", None, "star"],
        save_answers=False,
        orientation="vertical",
    )
