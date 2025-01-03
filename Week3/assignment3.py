#1:
def greet_user():
    name = input("Enter your name: ")
    if name:  # Check if name is not empty
        print(f"Hello, {name}!")
    else:
        print("Hello, Stranger!")

greet_user()

#2:
def set_password():
    password = input("Enter your new password: ")
    confirm_password = input("Confirm your new password: ")
    
    if password == confirm_password:
        print("Password Set")
    else:
        print("Error")

set_password()

#3:
def set_password():
    password = input("Enter your password from 8-12 characters: ")
    if 8 <= len(password) <= 12:
        print("Valid length for password")
    else:
        print(" Password must be between 8 and 12 character.")
        return  

    confirm_password = input("Confirm your new password: ")
    
    if password == confirm_password:
        print("Password Set")
    else:
        print("Error: Passwords do not match.")

set_password()

#4:
def set_password():
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

    password1 = input("Enter a password between 8-12 characters: ")

    if 8 <= len(password1) <= 12:
        if password1 not in BAD_PASSWORDS:
            password2 = input("Confirm your password: ")
            if password1 == password2:
                print("Password Set")
            else:
                print("Error: Passwords do not match")
        else:
            print("Error: Bad password")
    else:
        print("Error: Password must be between 8 and 12 characters.")
set_password()

#5:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    valid_length = 8 <= len(password) <= 12
    good_password = password not in BAD_PASSWORDS  
    final_password = password == confirm_password

    if valid_length and good_password and final_password:
        print("Password Set")
        break
    else:
        print("Invalid password")

#6:
num = int(input("Enter a number: "))
for i in range(0, 13):
    print(f"{i} x {num} = {i*num}")
    
#7:
num = int(input("Enter a number: "))
if num in range(0, 13):
    for i in range(0, 13):
        print(f"{i} x {num} = {i*num}")
else:
    print("Please enter a number between range 0-12")
    
#8:
num = int(input("Enter a number: "))

if num < 0:
    for i in range(12, -1, -1):
        print(f"{i} x {num} = {i*num}")
else:

    for i in range(0,13):
        print(f"{i} x {num} = {i*num}")




