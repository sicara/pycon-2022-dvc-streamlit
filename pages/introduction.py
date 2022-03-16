import streamlit_book as stb

# Streamlit book properties
stb.set_book_config(
    menu_title="Introduction",
    menu_icon="book",
    options=[
        "Who I am ?",
        "ML engineers are Software engineers ...",
        "... but ML is different from classical Software engineering",
    ],
    paths=[
        "pages/introduction/whoiam.py",
        "pages/introduction/ml_engineers_are_software_engineers.py",
        "pages/introduction/ml_is_different_from_software_engineering.py",
    ],
    save_answers=False,
    orientation="vertical",
)
