import hashlib

class User:
    def __init__(self, username, password, status=True):
        self.username = username
        self.password = password
        self.status = status

users = []

def add_user():
    new_username = input("Choose a Username: ")
    while new_username in [user.username for user in users]:
        new_username = input("Username already in use; choose a different username: ")
    
    password = input("Choose a 4 character password: ")
    while len(password) != 4:
        print("Password must be exactly 4 characters long.")
        password = input("Choose a 4 character password: ")

    accessword = input("Please provide a secondary password with any characters: ")
    
    first_name = input("First name? ")
    last_name = input("Last name? ")
    
    username = User(new_username, password)
    full_name = first_name + " " + last_name
    User_info = {"Full Name": full_name, "Password": password, "Username": new_username}
    users.append(username)
    print("User successfully added.")

def login():
    username_entry = input("Please provide username: ")
    found_user = next((user for user in users if user.username == username_entry), None)
    
    if found_user is None:
        print("User not found.")
        return
    
    if not found_user.status:
        print("Account locked.")
        return

    password_count = 0
    while password_count < 4:
        password_entry = input("Password? ")
        if password_entry == found_user.password:
            print("Login details accepted. Welcome, " + found_user.username)
            break
        else:
            password_count += 1

    if password_count >= 4:
        print("Login attempts exceeded. Contact customer support for assistance.")
        found_user.status = False

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
