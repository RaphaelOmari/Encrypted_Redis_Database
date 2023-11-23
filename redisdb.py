from pymongo import MongoClient
import os

class MongoDBManager:
    def __init__(self):
        self.client = MongoClient(os.environ.get('MONGODB_URI'))
        self.db = self.client.user_management
        self.users_collection = self.db.users

    def find_user(self, username):
        return self.users_collection.find_one({"username": username})

    def update_user(self, username, update_data):
        self.users_collection.update_one({"username": username}, {"$set": update_data})

    def delete_user(self, username):
        self.users_collection.delete_one({"username": username})

    # Additional methods for aggregation, backup, etc.

# Example Usage
db_manager = MongoDBManager()
user_data = db_manager.find_user("sample_username")
print(user_data)