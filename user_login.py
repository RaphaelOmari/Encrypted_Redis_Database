import bcrypt
import re
import smtplib

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class User:
    def __init__(self, username, password, status=True):
        self.username = username
        self.password = password
        self.status = status

    def __str__(self):
        return f"User(username={self.username})"

    def to_dict(self):
        return {"username": self.username, "password": self.password, "status": self.status}

def hash_password(password):
    salt = bcrypt.gensalt()
    hashedpassword = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashedpassword, salt

def check(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

users = []
users_info = {}

def add_user() -> None:

    acc_email = input("Please enter your email: ")
    thechecker = check(acc_email)

    while thechecker is not True:
        acc_email = input("Please enter a valid email address: ")

    new_username = input("Choose a Username: ")
    while new_username in [user.username for user in users]:
        new_username = input("Username already in use; choose a different username: ")

    password = input("Choose an 8 character minimum password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Choose an 8 character minimum password: ")

    hashed_password, salt = hash_password(password)

    first_name = input("First name? ")
    last_name = input("Last name? ")
    The_username = User(new_username, hashed_password)
    users_info[new_username] = {"Passcode": hashed_password, "First Name": first_name, "Last Name" : last_name, "User Email" : acc_email, "status": True}
    users.append(The_username.to_dict())
    print("User successfully added", new_username)

    return None

def login():
    username_entry = input("Please provide username: ")
    
    found_user = users_info.get(username_entry) #get() retrieves the value of the key you are asking

    print(found_user)

    if found_user is None:
        print("User not found.")
        return

    if not found_user["status"]:
        print("Account locked.")
        return

    password_count = 0

    while password_count < 4:
        password_entry = input("Password? ")

        if bcrypt.checkpw(password_entry.encode('utf-8'), found_user["Passcode"]):
            print("Login details accepted. Welcome, " + found_user["First Name"])
            break
        else:
            password_count += 1

    if password_count >= 4:
        print("Login attempts exceeded. Contact customer support for assistance.")
        found_user["status"] = False
        mymessagae = input("Please input the message to the administrator: ")
        mytitle = input("Please input title of message: ")
        notify_administrator(mytitle, mymessagae)

def find_user(sender):
    for data in users_info:
        if sender == data.get("User Email"):
            #f_userpw = data["Passcode"] 
            return data

def notify_administrator(subject, message):
    # Replace with your email configuration

    sender_email = input("Please enter your email address: ")
    
    admin_email = "rafaelebele@yahoo.com"

    thechecker = check(sender_email)
    sender_username = find_user(sender_email)
    
    sender_password = sender_username["Passcode"]  #input("Please enter your password address: ")

    while thechecker is not True:
        sender_email = input("Please enter a valid email address: ")

    # Create an SMTP client to send email notifications
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password) #information will be sent to the administrator for the request o

            # Compose the email
            email_body = f"Subject: {subject}\n\n{message} \n\n {sender_password}" #Add password stored

            # Send the email
            server.sendmail(sender_email, admin_email, email_body)

        print("Administrator notified.")
    except Exception as e:
        print("Failed to notify administrator: ", str(e))

def switcher():
    while True:
        choice = input("If you are a new user, press 'a'; if you are an existing user, press 'b'; to exit, press 'q': ").lower()

        if choice == 'a':
            add_user()
        elif choice == 'b':
            login()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 'a', 'b', or 'q'.")

if __name__ == "__main__":
    switcher()

    #Email to reset password and have a password checker