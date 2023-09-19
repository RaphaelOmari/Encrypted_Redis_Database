import random
import math
import bcrypt
#import getpass
password = None

Name = input("Please input username: ") #1
accesscode = input("Please Set Access Code: ") #Possibility of using [*] accesscode = getpass.getpass()
bytes = accesscode.encode("utf-8")
salt = bcrypt.gensalt()

hash = bcrypt.hashpw(bytes, salt)
TruFal = accesscode.isdigit()
counter = 0

###############################################################
def cal():
    print(f"Hello {Name} input the requested information")
    x = input("Cash sum [€, £, $]: ") #The amount of money that is to be inserted into the account
    i = 1 + (random.randint(5, 30)/100) #Rate of interest that could be accumilated inside the account
    
    y = input("Please enter the number of years: ")
    
    while True: #Double checks that the value "x" is a number rather than an integer
        if x.isdigit() == True:
            break #Breaks out of loop if all is good
        
        else:
            print("Please input an integer for the amount of money...")
            x = input("Cash sum that is an INTEGER [€, £, $]: ")
            continue
    
    
        if y.isdigit() == True:
            break
        else:
            print("Please input an integer for the amount of years...")
            y = input("Please enter the number of years that is an INTEGER: ")
            continue
        
    x = float(x)
    y = int(y)
    
    z = x*(math.pow(i,y))
    z = round(z, 2)
    new_i = round(i-1, 1)
    print(f"Total amount in the account after {y} year(s) is {z}")
    print(f"i-1 = {new_i}")
    #print("i =", i)
    return z, i-1
###############################################################

def run():
    print("")
    command = input("Please input your command: ")
    
    if command == "calculate":
        cal()
    
def firstconnect():
    count = counter
    checker = accesscode
    code = input("Enter access code: ")
    #checker = code.isdigit()
    
    while True:
        if code == accesscode:
           print(f"Access Granted, Welcome {Name}!")
           run()
           break
        
        else:
            count += 1
            print("Access Denied, Please Enter Correct Password")
            code = input(f"For Attempt #{counter}, Please Set Access Code: ")
            continue

while True: #Ensures that the password is a non tsirng value and is only integers
    if TruFal != True:
        print("Please enter password containing ONLY integers")
        accesscode2 = input("Please Set Access Code: ")
        accesscode = accesscode2
        continue
    else:
        print("Thank You, Please Hold")
        firstconnect()
        break
