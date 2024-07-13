<<<<<<< HEAD
import pandas as pd

# Load data
user_interactions_df = pd.read_csv('data/user_interactions.csv')
content_metadata_df = pd.read_csv('data/content_metadata.csv')
social_connections_df = pd.read_csv('data/social_connections.csv')

# Data Cleaning
user_interactions_df.dropna(inplace=True)
content_metadata_df.dropna(inplace=True)
social_connections_df.dropna(inplace=True)

# Merge DataFrames
merged_df = pd.merge(user_interactions_df, content_metadata_df, on='content_id')
merged_df = pd.merge(merged_df, social_connections_df, on='user_id')

# Save cleaned data
merged_df.to_csv('data/merged_data.csv', index=False)
=======
import pandas as pd

# Load data
user_interactions_df = pd.read_csv('data/user_interactions.csv')
content_metadata_df = pd.read_csv('data/content_metadata.csv')
social_connections_df = pd.read_csv('data/social_connections.csv')

# Data Cleaning
user_interactions_df.dropna(inplace=True)
content_metadata_df.dropna(inplace=True)
social_connections_df.dropna(inplace=True)

# Merge DataFrames
merged_df = pd.merge(user_interactions_df, content_metadata_df, on='content_id')
merged_df = pd.merge(merged_df, social_connections_df, on='user_id')

# Save cleaned data
merged_df.to_csv('data/merged_data.csv', index=False)
>>>>>>> 21efe1b304df64857a2f6eefed48b3c39ac77c1c
