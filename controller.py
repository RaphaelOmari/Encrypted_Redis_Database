from getpass import getpass
from user_login import switcher, add_user, User

username = input("Please input your username: ")
password = getpass("Please input your password")

if __name__ == "__main__":
    switcher()
    tester()