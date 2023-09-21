import redisdb

class User():
    def __init__(self, first_name, last_name, username, password, accessword, status=True):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username  # Added username attribute
        self.password = password
        self.accessword = accessword
        self.name = first_name.title() + " " + last_name.title()
        self.status = status

users = []

def add_user():
    new_username = input("Choose a Username: ")
    while new_username in [user.username for user in users]:
        new_username = input("Username already in use; choose a different username: ")
    password = ""
    accessword = ""
    while len(password) != 4:
        password = input("Choose a 4 character password: ")

    while len(accessword) >= 8:
        accessword = input("Please provide a secondary password with any characters: ")

    first_name = input("First name? ")
    last_name = input("Last name? ")

    username = User(first_name, last_name, new_username, password, accessword)
    print("Welcome " + username.name)
    users.append(username)
    print(users)

    more = input("Add another user? (Y/N) ").lower()
    if more != "n" and more != "no":
        add_user()
    else:
        print("Username successfully added")

    return username


def login():
    username_entry = ""
    while username_entry not in [user.username for user in users]:
        username_entry = input("Please provide username: ")
    
    found_user = next(user for user in users if user.username == username_entry)
    
    if not found_user.status:
        print("Account locked")
    else:
        password_count = 0
        while password_count < 4:
            password_entry = input("Password? ")
            if password_entry == found_user.password:
                print("Login details accepted. Welcome " + found_user.name)
                break
            else:
                password_count += 1
        if password_count >= 4:
            print("Login attempts exceeded. Contact customer support for assistance.")
            found_user.status = False

    #more = input("Login user? (Y/N) ").lower()
    #if more != "n" and more != "no":
    #    login()

add_user()
login()
