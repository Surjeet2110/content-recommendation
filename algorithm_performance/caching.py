<<<<<<< HEAD
import redis
import pandas as pd

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# Load user profiles
user_profiles = pd.read_csv('data/user_profiles.csv')

# Cache frequently accessed data
for index, row in user_profiles.iterrows():
    cache.set(row['user_id'], row.to_json())
=======
import redis
import pandas as pd

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# Load user profiles
user_profiles = pd.read_csv('data/user_profiles.csv')

# Cache frequently accessed data
for index, row in user_profiles.iterrows():
    cache.set(row['user_id'], row.to_json())
>>>>>>> 21efe1b304df64857a2f6eefed48b3c39ac77c1c
