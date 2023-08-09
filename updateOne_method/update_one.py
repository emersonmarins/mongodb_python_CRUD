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

# Filter
document_to_update = { "_id": ObjectId("64cbd8a8e840d4ab4658b57b") }

# Update
add_to_balance = { "$inc": { "balance": 100 } }

# Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# Write an expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))
  
client.close()