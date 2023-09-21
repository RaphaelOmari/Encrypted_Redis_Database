import user_login
import hashlib

# Use the add_user() function to create a User object
new_user = user_login.add_user() #Ensure that the function has a return value

accesscode = ""

while len(accesscode) < 8:
    accesscode = input("Please provide Accesscode: ")

# Fetch the user's password attribute and convert it to bytes
password_bytes = new_user.password.encode('utf-8')

# Concatenate the accesscode and the password bytes before hashing
combined_data = accesscode.encode('utf-8') + password_bytes

# Hash the combined data
passwd = hashlib.sha1(combined_data).digest()

print(passwd)
