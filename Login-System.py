# login system

correct_username = "admin"
correct_password = "password123"

count = 0

while count < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")
        count += 1

if count == 3:
    print("Too many failed attempts. Please try again later.")