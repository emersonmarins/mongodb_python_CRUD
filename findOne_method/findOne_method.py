import os
import pprint
 
from dotenv import load_dotenv
from pymongo import MongoClient

# Import ObjectId from bson package (part of PyMongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file 
load_dotenv()
MONGODB_URI = os.environ['URI']

# Connect to MongoDB cluster with MongoClient
client =  MongoClient(MONGODB_URI)

# Get a reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = { "_id": ObjectId("64cbd8a8e840d4ab4658b57b") }

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)
print(f'document found: {result}')
    
client.close()