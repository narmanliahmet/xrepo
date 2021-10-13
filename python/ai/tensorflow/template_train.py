import os

import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)

#Get an example dataset
#To demonstrate how to save and load weights, you'll use the MNIST dataset. To speed up these runs, use the first 1000 examples:

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

#Define a model
#Start by building a simple sequential model:

# Define a simple sequential model
# Layers are subject to change////
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])

# Compile the model
  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.metrics.SparseCategoricalAccuracy()])

  return model

# Create a basic model instance
model = create_model()

# Display the model's architecture
model.summary()

# Save checkpoints during training
# You can use a trained model without having to retrain it, or pick-up training where you left off 
# in case the training process was interrupted. The tf.keras.callbacks.ModelCheckpoint callback
# allows you to continually save the model both during and at the end of training.

# Checkpoint callback usage
# Create a tf.keras.callbacks.ModelCheckpoint callback that saves weights only during training:

checkpoint_path = "model_sample/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Train the model with the new callback
model.fit(train_images, 
          train_labels,
          batch_size=None, 
          epochs=20,
          validation_data=(test_images, test_labels),
          callbacks=[cp_callback])  # Pass callback to training

# This may generate warnings related to saving the state of the optimizer.
# These warnings (and similar warnings throughout this notebook)
# are in place to discourage outdated usage, and can be ignored.

os.listdir(checkpoint_dir)