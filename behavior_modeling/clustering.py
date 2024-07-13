import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data/merged_data.csv')

# Feature selection
features = data[['interaction_type', 'content_type', 'connection_strength']]

# K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(features)
data['cluster'] = clusters

# Save clustered data
data.to_csv('data/clustered_data.csv', index=False)

# Visualization
plt.scatter(data['interaction_type'], data['content_type'], c=clusters, cmap='viridis')
plt.xlabel('Interaction Type')
plt.ylabel('Content Type')
plt.title('User Clusters')
plt.show()
