import cloudant
from pymongo import MongoClient

# Connect to Cloudant
cloudant_client = cloudant.Cloudant("apikey-v2-wlo84wtv6k4niy0zeqs6vkstccknujnhxwkoey2m09s", "54bfdf8b8ce1d263dbcd3032c7af80eb", url="https://apikey-v2-wlo84wtv6k4niy0zeqs6vkstccknujnhxwkoey2m09s:54bfdf8b8ce1d263dbcd3032c7af80eb@9480306c-6dfb-4b51-9ce7-e7450483dcb8-bluemix.cloudantnosqldb.appdomain.cloud")
cloudant_client.connect()
cloudant_db = cloudant_client['ats-dev']

# Connect to MongoDB
mongo_client = MongoClient("mongodb+srv://achmad4512:Zano2611@cluster0.wzxfiua.mongodb.net/?retryWrites=true&w=majority")
mongo_db = mongo_client['cloudant2mongo']

# Define a dictionary to map Cloudant types to MongoDB collections
collection_mapping = {
    "Application": "Application",
    "Blueform": "Blueform",
    "User": "User",
    "User-unverified": "User-unverified",
    "Job": "Job",
    "Test": "Test",
    "EVS": "EVS",
    "Contract": "Contract",
    "Hiring Form": "Hiring Form",
    "Recruiter": "Recruiter",
    "Notification": "Notification",
    "Onboarding_Form": "Onboarding_Form",
    "Testimomy": "Testimomy",
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
