import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="DVC + Streamlit",
        menu_icon="book",
        options=[
            "DVC + Streamlit = ❤️",
            "Retrieve experiment commits",
            "The table of experiments app",
            "Load experiment files",
            "A model diffing app",
            "A step back...",
        ],
        paths=[
            "pages/dvc_and_streamlit/dvc_and_streamlit_love.py",
            "pages/dvc_and_streamlit/retrieve_xp_commit.py",
            "pages/dvc_and_streamlit/xp_table_app.py",
            "pages/dvc_and_streamlit/load_xp_files.py",
            "pages/dvc_and_streamlit/model_diffing_app.py",
            "pages/dvc_and_streamlit/a_step_back.py",
        ],
        save_answers=False,
        orientation="vertical",
    )
