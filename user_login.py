import hashlib
import os
from pymongo import MongoClient

# Database Configuration
client = MongoClient(os.environ.get('MONGODB_URI'))
db = client.user_management
users_collection = db.users

class User:
    def __init__(self, first_name, last_name, username, password_hash, accessword_hash, status=True):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password_hash = password_hash
        self.accessword_hash = accessword_hash
        self.status = status
        counter = 0

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password_hash": self.password_hash,
            "accessword_hash": self.accessword_hash,
            "status": self.status
        }

def hash_password(password):
    salt = os.urandom(32)
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def add_user():
    new_username = input("Choose a Username: ")
    while users_collection.find_one({"username": new_username}):
        new_username = input("Username already in use; choose a different username: ")
    
    password = input("Choose a 4 character password: ")
    while len(password) != 4:
        password = input("Password must be 4 characters: ")
    
    accessword = input("Please provide a secondary password with any characters: ")
    while len(accessword) < 8:
        accessword = input("Secondary password must be at least 8 characters: ")

    first_name = input("First name? ")
    last_name = input("Last name? ")

    password_hash = hash_password(password)
    accessword_hash = hash_password(accessword)

    new_user = User(first_name, last_name, new_username, password_hash, accessword_hash)
    users_collection.insert_one(new_user.to_dict())
    print(f"Welcome {new_user.first_name} {new_user.last_name}")

Locked_Users = {}

def login():
    username_entry = input("Please provide username: ")
    user_data = users_collection.find_one({"username": username_entry})
    
    if user_data:
        found_user = User(**user_data) #Kwarg
        if not found_user.status:
            print("Account locked")
            return
        
        while True:
            password_entry = input("Enter Password: ")
            if hashlib.pbkdf2_hmac('sha256', password_entry.encode(), found_user.password_hash[:32], 100000) == found_user.password_hash:
                print(f"Login details accepted. Welcome {found_user.first_name} {found_user.last_name}")
            else:
                print("Incorrect password")
                found_user.counter += 1
                # Implement logic to lock account after certain attempts
                if found_user.counter = 3:
                    found_user.status = "False" #Locked account
                    Locked_Users.insert_one(found_user) #Add user to a list of accounts that have been locked due to too many attempts


    else:
        print("Username not found")

add_user()
login()
