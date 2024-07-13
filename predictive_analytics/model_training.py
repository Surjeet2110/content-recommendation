import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load user profiles
user_profiles = pd.read_csv('data/user_profiles.csv')

# Prepare data
X = user_profiles[['interaction_type', 'content_type', 'connection_strength']]
y = user_profiles['user_id']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save model
model.save('models/recommendation_model.h5')

