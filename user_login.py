import hashlib
import random
import string

class User:
    def __init__(self, username, password, status=True):
        self.username = username
        self.password = password
        self.status = status

    def __str__(self):
        return f"User(username={self.username})"

    def to_dict(self):
        return {"username": self.username, "password": self.password}

users = []

def add_user():
    new_username = input("Choose a Username: ")
    while new_username in [user.username for user in users]:
        new_username = input("Username already in use; choose a different username: ")

    password = input("Choose a 4 character password: ")
    while len(password) != 4:
        print("Password must be exactly 4 characters long.")
        password = input("Choose a 4 character password: ")

    salt = 'Hex10'
    db_password = password + salt
    hashed = hashlib.md5(db_password.encode())

    first_name = input("First name? ")
    last_name = input("Last name? ")
    The_username = User(new_username, hashed.hexdigest())  # Store the hashed password
    user_dict = The_username.to_dict()
    user_dict["status"] = True  # Add the 'status' field
    full_name = first_name + " " + last_name
    users.append(user_dict)
    print("User successfully added", The_username.username)

def login():
    username_entry = input("Please provide username: ")
    found_user = next((user for user in users if user["username"] == username_entry), None)
    salt = 'Hex10'

    if found_user is None:
        print("User not found.")
        return

    if not found_user["status"]:
        print("Account locked.")
        return

    password_count = 0

    while password_count < 4:
        password_entry = input("Password? ")
        db_password = password_entry + salt
        hashedpw = hashlib.md5(db_password.encode())

        if hashedpw.hexdigest() == found_user["password"]:
            print("Login details accepted. Welcome, " + found_user["username"])
            break
        else:
            password_count += 1

    if password_count >= 4:
        print("Login attempts exceeded. Contact customer support for assistance.")
        found_user["status"] = False

def switcher():
    while True:
        choice = input("If you are a new user, press 'a'; if you are an existing user, press 'b': ").lower()

        if choice == 'a':
            add_user()
        elif choice == 'b':
            login()
        else:
            print("Invalid choice. Please select 'a' or 'b'.")

if __name__ == "__main__":
    switcher()
