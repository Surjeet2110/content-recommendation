<<<<<<< HEAD
import pandas as pd

# Load clustered data
data = pd.read_csv('data/clustered_data.csv')

# Create user profiles
user_profiles = data.groupby('user_id').agg({
    'interaction_type': 'sum',
    'content_type': 'sum',
    'connection_strength': 'mean'
}).reset_index()

# Save user profiles
user_profiles.to_csv('data/user_profiles.csv', index=False)
=======
import pandas as pd

# Load clustered data
data = pd.read_csv('data/clustered_data.csv')

# Create user profiles
user_profiles = data.groupby('user_id').agg({
    'interaction_type': 'sum',
    'content_type': 'sum',
    'connection_strength': 'mean'
}).reset_index()

# Save user profiles
user_profiles.to_csv('data/user_profiles.csv', index=False)
>>>>>>> 21efe1b304df64857a2f6eefed48b3c39ac77c1c
