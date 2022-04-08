import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="DVC",
        menu_icon="book",
        options=[
            "Classifying cats and dogs",
            "The cats vs dogs dataset",
            "The training pipeline",
            "Run an experiment! (first try)",
            "DVC, help us! (1/2)",
            "DVC, help us! (2/2)",
            "An experiment = a DVC Pipeline",
            "Run an experiment! (second try)",
            "Dealing with non-linear workflow",
            "Introducing DVC experiments",
            "See the experiment table",
            "Run an experiment! (third and last try)",
            "A step back...",
        ],
        paths=[
            "pages/dvc_training_pipeline/introducing_the_problem.py",
            "pages/dvc_training_pipeline/dataset.py",
            "pages/dvc_training_pipeline/introducing_the_scripts.py",
            "pages/dvc_training_pipeline/run_an_experiment_step_0.py",
            "pages/dvc_training_pipeline/what_is_dvc.py",
            "pages/dvc_training_pipeline/what_is_dvc_2.py",
            "pages/dvc_training_pipeline/introducing_the_training_pipeline.py",
            "pages/dvc_training_pipeline/run_an_experiment_step_1.py",
            "pages/dvc_training_pipeline/non_linear_workflow.py",
            "pages/dvc_training_pipeline/introducing_dvc_exp.py",
            "pages/dvc_training_pipeline/try_dvc_exp.py",
            "pages/dvc_training_pipeline/run_an_experiment_step_2.py",
            "pages/dvc_training_pipeline/a_step_back.py",
        ],
        save_answers=False,
        orientation="vertical",
    )
