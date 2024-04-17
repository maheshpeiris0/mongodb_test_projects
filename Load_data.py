import json
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace 'mydatabase' with your database name
collection = db['mycollection']  # Replace 'mycollection' with your collection name

# Step 2: Load JSON data
with open('data.json', 'r') as file:
    file_data = json.load(file)

# Step 3: Insert data into the collection
# If file_data is a list of dictionaries
if isinstance(file_data, list):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)

# Close the connection
client.close()
