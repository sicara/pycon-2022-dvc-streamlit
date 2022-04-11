from pathlib import Path

AUTHOR = "Antoine Toubhans"
CONFERENCE_DATE = "April 12th, 2022"
CONFERENCE_NAME = "PyData Berlin 2022"
TITLE = "Flexible ML Experiment Tracking System for Python Coders with DVC and Streamlit"
TITLE_SHORT = "DVC + Streamlit = ❤️"

ROOT_DIR = Path(__file__).resolve().parent
IMAGES_DIR = ROOT_DIR / "images"
PAGES_DIR = ROOT_DIR / "pages"
CODE_SAMPLES_DIR = ROOT_DIR / "code_samples"

CONFERENCE_LOGO_PATH = IMAGES_DIR / "PyConDE_PyDataBer_circle_trans_500.png"
CONFERENCE_FULL_LOGO_PATH = IMAGES_DIR / "PyConDEPyDataBER-1800-transparent.png"

# CSS STYLES
FULL_HEIGHT_PIXELS = 760

# Pipeline code
CODE_DIR = ROOT_DIR / "src"
PIPELINE_PATH = CODE_DIR / "dvc.yaml"
PARAMS_PATH = CODE_DIR / "params.yaml"

# Pages
CHAPTER_INTRODUCTION = "1️⃣ Introduction"
CHAPTER_ML_PIPELINE = "2️⃣ Let's do ML!"
CHAPTER_ML_ANALYSIS = "3️⃣ Let's build a UI!"
CHAPTER_DVC_AND_STREAMLIT = "4️⃣ DVC + Streamlit = ❤️"
CHAPTER_CONCLUSION = "5️⃣ Conclusion"

CHAPTERS = [
    CHAPTER_INTRODUCTION,
    CHAPTER_ML_PIPELINE,
    CHAPTER_ML_ANALYSIS,
    CHAPTER_DVC_AND_STREAMLIT,
    CHAPTER_CONCLUSION,
]
