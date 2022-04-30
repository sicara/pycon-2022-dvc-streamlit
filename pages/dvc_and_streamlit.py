import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="DVC + Streamlit",
        menu_icon="book",
        options=[
            "DVC + Streamlit = ❤️",
            "The table of experiments app",
            "Retrieve experiment commits",
            "A model diffing app",
            "Load experiment files",
        ],
        paths=[
            "pages/dvc_and_streamlit/dvc_and_streamlit_love.py",
            "pages/dvc_and_streamlit/xp_table_app.py",
            "pages/dvc_and_streamlit/retrieve_xp_commit.py",
            "pages/dvc_and_streamlit/model_diffing_app.py",
            "pages/dvc_and_streamlit/load_xp_files.py",
        ],
        save_answers=False,
        orientation="vertical",
    )
