import datetime
import os

from pymongo import MongoClient
from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
MONGO_URI = os.environ['URI']

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGO_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Alice Manuella",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 2434,
    "last_updated": datetime.datetime.utcnow(),
}

result = accounts_collection.insert_one(new_account)
document_id = result.inserted_id
print(f'_id of result document: {document_id}')

client.close()