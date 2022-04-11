import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

IMG_SIZE = (160, 160)

# Load the model only once!
@st.experimental_singleton
def load_model():
    import tensorflow as tf

    from constants import CODE_DIR

    return tf.keras.models.load_model(
        CODE_DIR / "data" / "train" / "model"
    )


model = load_model()

uploaded_file = st.file_uploader("Upload an image")

if uploaded_file:
    image = Image.open(uploaded_file)
    image_name = uploaded_file.name
    resized_image = image.resize(IMG_SIZE)

    st.image(image, caption="Original image")
    st.image(resized_image, caption=f"Resized image: {IMG_SIZE}")

    input = np.expand_dims(
        tf.keras.preprocessing.image.img_to_array(resized_image),
        axis=0
    )

    predictions = []

    prediction = tf.nn.sigmoid(model.predict(input).flatten()).numpy()[0]
    st.write(f"Prediction: {prediction}")

    predicted_label = "dog" if prediction > 0.5 else "cat"
    st.write(f"Predicted label: {predicted_label}")
