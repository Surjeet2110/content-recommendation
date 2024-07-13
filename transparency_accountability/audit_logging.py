import logging

# Set up logging
logging.basicConfig(filename='recommendation_audit.log', level=logging.INFO)

# Log recommendations
logging.info('User ID: 1, Recommended Content: [101, 102, 103]')