import dvc.repo
import git
import streamlit as st

from constants import ROOT_DIR


def st_show():
    st.write("TODO")

    #
    GIT_REPO = git.Repo(str(ROOT_DIR))
    DVC_REPO = dvc.repo.Repo(ROOT_DIR)

    FIRST_COMMIT = "41b2e0b3584b8acaea8da33e0ebc17800cb59203"

    #%% Retrive commits for trained model
    MODELS_COMMITS = list(
        GIT_REPO.iter_commits(
            rev=f"...{FIRST_COMMIT}",
            paths="src/dvc.lock",
        )
    )

    st.write("Commits:")
    st.write(MODELS_COMMITS)

    #%%
    st.write("Exps")


#    st.write(DVC_REPO.experiments.ls(all_=True))
#    st.write(DVC_REPO.experiments.show(all_commits=True))
