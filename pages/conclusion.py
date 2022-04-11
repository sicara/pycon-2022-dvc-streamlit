import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Conclusion",
        menu_icon="book",
        options=[
            "A step back...",
            "Pros & cons",
            "Thanks :)",
        ],
        paths=[
            "pages/conclusion/a_step_back.py",
            "pages/conclusion/pro_and_cons.py",
            "pages/conclusion/thanks.py",
        ],
        save_answers=False,
        orientation="vertical",
    )
