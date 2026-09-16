# this syntax is loop syntax in Python. It is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in that sequence. The variable takes on the value of each item in the sequence one at a time, allowing you to perform operations on each item.


# for variable in something:
    # code

for i in range(5):
    print("Hello")

for i in range(1, 6):
    print(i)

# range(start, stop, step)
for i in range(0, 11, 2):
    print(i)


name = "Python"

for letter in name:
    print(letter)


languages = ["Python", "JavaScript", "Java"]

for language in languages:
    print(language)


count = 1

while count <= 5:
    print(count)
    count = count + 1