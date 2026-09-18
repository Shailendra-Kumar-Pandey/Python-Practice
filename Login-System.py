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



# if       → check a condition
# elif     → check another condition
# else     → otherwise

# for      → repeat/iterate
# while    → repeat while condition is true

# break    → completely stop loop
# continue → skip current iteration

# ==       → compare equality
# =        → assign value

# and      → both conditions
# or       → at least one condition
# not      → reverse condition