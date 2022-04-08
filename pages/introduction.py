import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Introduction",
        menu_icon="book",
        options=[
            "Who am I?",
            "What is machine learning engineering?",
            "ML engineering is more than software engineering",
            "Tracking ML experiments",
            "What I am not going to talk about today",
            "What I am going to talk about today",
        ],
        paths=[
            "pages/introduction/whoiam.py",
            "pages/introduction/ml_engineers_are_software_engineers.py",
            "pages/introduction/ml_is_different_from_software_engineering.py",
            "pages/introduction/what_is_xp_tracking.py",
            "pages/introduction/what_iam_not_going_to_talk.py",
            "pages/introduction/what_iam_going_to_talk.py",
        ],
        icons=["person"],
        save_answers=False,
        orientation="vertical",
    )
