import pandas as pd
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric

# Load user profiles
user_profiles = pd.read_csv('data/user_profiles.csv')

# Convert to BinaryLabelDataset
data = BinaryLabelDataset(df=user_profiles, label_names=['interaction_type'], protected_attribute_names=['gender'])

# Fairness metrics
metric = BinaryLabelDatasetMetric(data, privileged_groups=[{'gender': 1}], unprivileged_groups=[{'gender': 0}])
print(metric.mean_difference())
