<<<<<<< HEAD
import pandas as pd
import shap
import tensorflow as tf

# Load data
user_profiles = pd.read_csv('data/user_profiles.csv')
X = user_profiles[['interaction_type', 'content_type', 'connection_strength']]

# Load model
model = tf.keras.models.load_model('models/recommendation_model.h5')

# Explain model predictions
explainer = shap.KernelExplainer(model.predict, X)
shap_values = explainer.shap_values(X)

# Plot SHAP values
shap.summary_plot(shap_values, X)
=======
import pandas as pd
import shap
import tensorflow as tf

# Load data
user_profiles = pd.read_csv('data/user_profiles.csv')
X = user_profiles[['interaction_type', 'content_type', 'connection_strength']]

# Load model
model = tf.keras.models.load_model('models/recommendation_model.h5')

# Explain model predictions
explainer = shap.KernelExplainer(model.predict, X)
shap_values = explainer.shap_values(X)

# Plot SHAP values
shap.summary_plot(shap_values, X)
>>>>>>> 21efe1b304df64857a2f6eefed48b3c39ac77c1c
