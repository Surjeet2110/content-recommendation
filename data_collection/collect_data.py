import pandas as pd

# Mock data for user interactions
user_interactions = [
    {'user_id': 1, 'content_id': 101, 'interaction_type': 'like'},
    {'user_id': 2, 'content_id': 102, 'interaction_type': 'view'},
    {'user_id': 1, 'content_id': 103, 'interaction_type': 'comment'},
    {'user_id': 3, 'content_id': 101, 'interaction_type': 'share'},
]

user_profiles = [
    {'user_id': 1, 'age': 25, 'gender': 'female'},
    {'user_id': 2, 'age': 30, 'gender': 'male'},
    {'user_id': 3, 'age': 22, 'gender': 'female'},
]

content_metadata = [
    {'content_id': 101, 'category': 'technology', 'length': 5},
    {'content_id': 102, 'category': 'health', 'length': 3},
    {'content_id': 103, 'category': 'sports', 'length': 7},
]

# Convert to DataFrame
user_interactions_df = pd.DataFrame(user_interactions)
user_profiles_df = pd.DataFrame(user_profiles)
content_metadata_df = pd.DataFrame(content_metadata)

# Save to CSV files
user_interactions_df.to_csv('data/user_interactions.csv', index=False)
user_profiles_df.to_csv('data/user_profiles.csv', index=False)
content_metadata_df.to_csv('data/content_metadata.csv', index=False)

print("Mock data saved to CSV files.")
