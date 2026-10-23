import os

def insecure_function():
    user_input = input("Enter directory to list: ")
    os.system("ls " + user_input)

def another_insecure():
    password = "123456"
    print("Password is", password)

def secure_function():
    print("Hello, Secure World!")

another_insecure()