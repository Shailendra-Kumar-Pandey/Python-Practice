age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")



x = 10

print(x == 10)
print(x != 5)
print(x > 5)
print(x < 20)
print(x >= 10)
print(x <= 10)



# Logical operators


age = 25
has_id = True

if age >= 18 and has_id:
    print("Access allowed")
else:
    print("Access denied")




day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")



is_logged_in = False

if not is_logged_in:
    print("Please login")



age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("You are under 18")