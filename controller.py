from user_login import *
from getpass import getpass

username = input("Please input your username: ")
password = getpass("Please input your password")

mylogin = user_login.User(username, password)

mylogin.switcher()






