import streamlit_book as stb

# Streamlit book properties
stb.set_book_config(
    menu_title="Training Pipeline",
    menu_icon="book",
    options=[
        "Classifying Cats and Dogs",
        "Introducing the Training Pipeline",
    ],
    paths=[
        "pages/dvc_training_pipeline/introducing_the_problem.py",
        "pages/dvc_training_pipeline/introducing_the_training_pipeline.py",
    ],
    save_answers=False,
    orientation="vertical",
)
