import bcrypt
import pymongo
from user_login import add_user

# MongoDB connection string
mongo_uri = "mongodb://localhost:27017/"

# Initialize the MongoDB client
client = pymongo.MongoClient(mongo_uri)

# Select or create a database
db = client["key_management"]

# Select or create a collection for keys
keys_collection = db["keys"]

def generate_encryption_key():
    # Generate a new encryption key
    key = bcrypt.gensalt()
    return key

def store_key_securely(key_name, key):
    # Store the key securely in MongoDB
    key_document = {"name": key_name, "key": key.decode('utf-8')}
    keys_collection.insert_one(key_document)
    print(f"Key '{key_name}' securely stored in MongoDB.")

def backup_key(key_name, key):
    # Simulate backing up the key securely (e.g., to a backup server or secure storage)
    # In practice, this would involve encryption and secure transmission/storage
    print(f"Key '{key_name}' backed up securely.")

def recover_key(key_name):
    # Retrieve the key from MongoDB
    key_document = keys_collection.find_one({"name": key_name})
    if key_document:
        recovered_key = key_document["key"].encode('utf-8')
        print(f"Key '{key_name}' recovered successfully from MongoDB.")
        return recovered_key
    else:
        print(f"Key '{key_name}' not found in MongoDB backup.")
        return None

if __name__ == "__main__":
    # Generate a new encryption key
    encryption_key = generate_encryption_key()

    # Store the encryption key securely in MongoDB
    store_key_securely("main_key", encryption_key)

    # Simulate a backup operation
    backup_key("main_key", encryption_key)

    # Simulate a key recovery operation
    recovered_key = recover_key("main_key")

    if recovered_key:
        # Use the recovered key for decryption or other operations
        print("Using recovered key for decryption.")
    else:
        print("Key recovery failed. Contact support for assistance.")

# Close the MongoDB client when done
client.close()

