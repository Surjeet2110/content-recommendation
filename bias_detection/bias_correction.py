<<<<<<< HEAD
import numpy as np
import pandas as pd

# Load user profiles
user_profiles = pd.read_csv('data/user_profiles.csv')

# Reweighting based on bias analysis
weights = np.where(user_profiles['gender'] == 1, 0.5, 1.0)
user_profiles['weights'] = weights

# Save weighted user profiles
user_profiles.to_csv('data/weighted_user_profiles.csv', index=False)
=======
import numpy as np
import pandas as pd

# Load user profiles
user_profiles = pd.read_csv('data/user_profiles.csv')

# Reweighting based on bias analysis
weights = np.where(user_profiles['gender'] == 1, 0.5, 1.0)
user_profiles['weights'] = weights

# Save weighted user profiles
user_profiles.to_csv('data/weighted_user_profiles.csv', index=False)
>>>>>>> 21efe1b304df64857a2f6eefed48b3c39ac77c1c
