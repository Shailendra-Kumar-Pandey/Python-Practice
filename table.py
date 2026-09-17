number = int(input("Which number table do you want: "))

for i in range(1, 11):
    print(number, "*", i, "=", number * i)



count = int(input("Enter the number: "))

while count > 0:
    print(count)
    count -= 1