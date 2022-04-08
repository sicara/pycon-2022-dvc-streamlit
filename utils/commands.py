from typing import Optional

import streamlit as st

from utils.html_factory import CSSStyle, make_div, st_write_bs4


def st_command(label: Optional[str] = None, initial_command: Optional[str] = None):
    import subprocess

    label = label or "Enter a command"
    initial_command = initial_command or ""

    command_column, button_column = st.columns([9, 1])
    command = command_column.text_input(label=label, value=initial_command)
    with button_column:
        st.write("")
        st.write("")
        is_clicked = st.button("Run !", disabled=command is "", key=label)

    if command != "" and is_clicked:
        with st.spinner(text=f"Running '{command}'"):
            result = subprocess.run(command.split(" "), capture_output=True, text=True)
            try:
                result.check_returncode()
                st_write_bs4(
                    make_div(
                        text=result.stdout,
                        style=CSSStyle(
                            color="white",
                            background_color="black",
                            white_space="pre",
                            overflow="scroll",
                            border_left="20px solid #32a854",
                            border_radius="10px",
                            padding_left="5px",
                        ),
                    )
                )
            except subprocess.CalledProcessError as e:
                st.error(result.stderr)
