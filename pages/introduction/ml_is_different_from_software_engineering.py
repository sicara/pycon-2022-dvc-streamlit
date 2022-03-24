import streamlit as st

command = st.text_input("Enter a command")


def run_command(command: str):
    import subprocess

    st.info(f"Running '{command}'")
    result = subprocess.run(command.split(" "), capture_output=True, text=True)
    try:
        result.check_returncode()
        st.text(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(result.stderr)


if command:
    run_command(command)
