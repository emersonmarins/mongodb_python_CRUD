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


new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "João Miguel",
        "account_type": "checking",
        "balance": 6218,
        "last_updated": datetime.datetime.utcnow(),
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Clarisse Vitória",
        "account_type": "savings",
        "balance": 14296,
        "last_updated": datetime.datetime.utcnow(),
    },
]

result = accounts_collection.insert_many(new_accounts)
accounts_id = result.inserted_ids
print(f'insert {str(len(accounts_id))} accounts')
print(f'_ids of inserted documents: {accounts_id}')

client.close()