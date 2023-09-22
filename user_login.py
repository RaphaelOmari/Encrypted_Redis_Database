import redisdb

class User():
    def __init__(self, username, password, status=True):
        
        self.username = username  # Added username attribute
        self.password = password
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

    username = User(new_username, password) #Seen as (username, password)

    full_name = first_name + last_name
    #print("Welcome " + username.name) username.name is how you reference the variable 
    User_info = {"Full Name" : full_name, "Password": password, "Username" : new_username}
    print("This is my try", User_info.values())
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

def switcher():
    mychoice = {"a": add_user, "b" : login}
    keylist = list(mychoice.keys())
    choice = input("If you are a new user please press 'a', if you are an existing user please press 'b'").lower()

    while mychoice not in  keylist:
        choice = input("If you are a new user please press 'a', if you are an existing user please press 'b'").lower()

    final_choice = mychoice[choice]()

    final_choice
    return None

#add_user()
#login()
