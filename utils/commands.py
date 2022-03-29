from typing import Optional

import streamlit as st


def st_command(label: Optional[str] = None, initial_command: Optional[str] = None):
    import subprocess

    label = label or "Enter a command"
    initial_command = initial_command or ""

    command = st.text_input(label=label, value=initial_command)

    if command:
        st.info(f"Running '{command}'")
        result = subprocess.run(command.split(" "), capture_output=True, text=True)
        try:
            result.check_returncode()
            st.text(result.stdout)
        except subprocess.CalledProcessError as e:
            st.error(result.stderr)
