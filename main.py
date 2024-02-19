import cloudant
from pymongo import MongoClient

# Connect to Cloudant
cloudant_client = cloudant.Cloudant("your_cloudant_username", "your_cloudant_password", url="your_cloudant_url")
cloudant_client.connect()
cloudant_db = cloudant_client['your_cloudant_database']

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client['your_mongodb_database']

# Define a dictionary to map Cloudant types to MongoDB collections
collection_mapping = {
    "type1": "collection1",
    "type2": "collection2",
    # Add more mappings as needed
}

# Iterate over each document in Cloudant
for document in cloudant_db:
    # Get the type of the document
    doc_type = document.get("type")

    # Check if the type has a corresponding MongoDB collection
    if doc_type in collection_mapping:
        # Get or create the MongoDB collection
        mongo_collection = mongo_db[collection_mapping[doc_type]]
        
        # Insert the document into the appropriate MongoDB collection
        mongo_collection.insert_one(document)

# Disconnect from databases
cloudant_client.disconnect()
mongo_client.close()

print("Migration completed successfully.")
