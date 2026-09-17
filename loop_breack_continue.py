# break use in loop

for i in range(1, 11):

    if i == 5:
        break

    print(i)


# continue use in loop
for i in range(1, 6):

    if i == 3:
        continue

    print(i)


password = ""

while password != "1234":
    password = input("Enter password: ")