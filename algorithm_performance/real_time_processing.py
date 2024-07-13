# real_time_processing.py
import json
from kafka import KafkaConsumer, KafkaProducer
import redis
import time

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# Kafka consumer to consume user interactions
consumer = KafkaConsumer(
    'user-interactions',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='user-interactions-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Kafka producer to produce recommendations
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Function to process user interactions and produce recommendations
def process_interaction(interaction):
    user_id = interaction['user_id']
    content_id = interaction['content_id']
    interaction_type = interaction['interaction_type']
    
    # Here you would process the interaction and generate recommendations
    # For simplicity, we just echo the interaction as a recommendation
    recommendations = {
        'user_id': user_id,
        'recommended_content': [content_id]  # Dummy recommendation
    }
    
    # Cache the recommendation in Redis
    cache.set(f'recommendations:{user_id}', json.dumps(recommendations))
    
    # Produce the recommendation to the Kafka topic
    producer.send('recommendations', value=recommendations)
    producer.flush()

# Consume user interactions and process them in real-time
for message in consumer:
    interaction = message.value
    process_interaction(interaction)
    print(f"Processed interaction: {interaction}")

# Note: Remember to install the necessary dependencies
# pip install kafka-python redis
