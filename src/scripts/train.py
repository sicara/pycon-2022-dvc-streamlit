# Original code from: https://www.tensorflow.org/tutorials/images/transfer_learning
import random

import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.keras.preprocessing import image_dataset_from_directory

from scripts.params import (
    BACKBONE,
    BATCH_SIZE,
    DATASET_DIR,
    EPOCHS_FROZEN,
    EPOCHS_UNFROZEN,
    FINE_TUNE_AT,
    IMG_SIZE,
    LEARNING_RATE,
    PREPROCESS_INPUT,
    TRAIN_DIR,
    TRAIN_SEED,
)

#%% Set random seed
print("Setting random seed:", TRAIN_SEED)
random.seed(TRAIN_SEED)
np.random.seed(TRAIN_SEED)
tf.random.set_seed(TRAIN_SEED)


#%% Load dataset
train_dataset = image_dataset_from_directory(
    DATASET_DIR / "train",
    shuffle=True,
    batch_size=BATCH_SIZE,
    image_size=IMG_SIZE,
).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

validation_dataset = image_dataset_from_directory(
    DATASET_DIR / "val",
    shuffle=True,
    batch_size=BATCH_SIZE,
    image_size=IMG_SIZE,
).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)


#%% Define model
# Data augmentation layers
data_augmentation = tf.keras.Sequential(
    [
        tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal"),
        tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
    ]
)

# Create the base model from the pre-trained model MobileNet V2
IMG_SHAPE = IMG_SIZE + (3,)
base_model = BACKBONE(input_shape=IMG_SHAPE, include_top=False, weights="imagenet")

inputs = tf.keras.Input(shape=IMG_SHAPE)
x = data_augmentation(inputs)
x = PREPROCESS_INPUT(x)
x = base_model(x, training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(1)(x)

model = tf.keras.Model(inputs, outputs)

callbacks = [
    TensorBoard(TRAIN_DIR / "tensorboard"),
    ModelCheckpoint(str(TRAIN_DIR / "best_weights.h5"), save_best_only=True),
]


#%% Freeze the base model and train EPOCHS_FROZEN epochs
if EPOCHS_FROZEN > 0:
    base_model.trainable = False

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )
    model.summary()

    history = model.fit(
        train_dataset,
        epochs=EPOCHS_FROZEN,
        validation_data=validation_dataset,
        callbacks=callbacks,
    )


if EPOCHS_UNFROZEN:
    #%% Unfreeze the base model
    base_model.trainable = True

    # Let's take a look to see how many layers are in the base model
    print("Number of layers in the base model: ", len(base_model.layers))

    # Freeze all the layers before the `FINE_TUNE_AT` layer
    for layer in base_model.layers[:FINE_TUNE_AT]:
        layer.trainable = False

    model.compile(
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        optimizer=tf.keras.optimizers.RMSprop(lr=LEARNING_RATE / 10),
        metrics=["accuracy"],
    )
    model.summary()

    history_fine = model.fit(
        train_dataset,
        epochs=EPOCHS_FROZEN + EPOCHS_UNFROZEN,
        initial_epoch=EPOCHS_FROZEN,
        validation_data=validation_dataset,
        callbacks=callbacks,
    )


#%% Load best weights and save model
model.load_weights(str(TRAIN_DIR / "best_weights.h5"))
model.save(str(TRAIN_DIR / "model"))
