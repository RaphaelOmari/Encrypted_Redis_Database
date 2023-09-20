#User log in list used

class User():
    def __init__(self, first_name, last_name, username, password, status=True):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.name = first_name.title() + " " + last_name.title()       

users = [ ]

def add_user():
    new_username = input("Choose a Username: ")    
    while new_username in users:
        new_username = input("Username already in use; choose a different username: ")
    password = ""
    while len(password) != 4:
        password = input("Choose a 4 character password: ")
    first_name = input("First name? ")
    last_name = input("Last name? ")

    username = User(first_name, last_name, new_username, password)
    print("Welcome " + username.name)
    users.append(new_username)
    print(users)

    more = input("Add another user? (Y/N) ").lower()
    if more != ("n" or "no"):
        add_user()

def login():
    username_entry = ""
    while username_entry not in users:
        username_entry = input("Username? ")
    if User(username_entry).status == False:
        print("Account locked")
    else:
        password_count = 0
        password_entry = ""
        if password_count < 4:
            while password_entry != username_entry.password:
                password_entry = input("Password? ")
                password_entry += 1
            print("Login details accepted. Welcome " + username_entry.name)
        else:
            print("Login attempts exceeded.  Contact customer support for assistance.")
            username_entry.status=False

    more = input("Login user? (Y/N) ").lower()
    if more != ("n" or "no"):
        login()

add_user()
login() 