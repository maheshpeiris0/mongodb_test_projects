import os
from pymongo.mongo_client import MongoClient

user_name=os.getenv('MONGO_DB_PS')
password=os.getenv('MONGO_DB_USER')

uri = f"mongodb+srv://{user_name}:{password}@cluster0.k7drlsg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)