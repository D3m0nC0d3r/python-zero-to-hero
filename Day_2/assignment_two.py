# Assignment - Take a string input and print the number of occurrences of each character.
# e.g: If string is "hello" then output should be h - 1, e - 1, l - 2, o - 1.

# taking user input
s = input("Enter a string: ")

# adding each character from user input string, and store it into set variable for avoid duplicate values.
unique_value = set(x for x in s)


# looping/iterating each character from set variable and checking the occurences in the user input string
for alpha in unique_value:
    print(f"{alpha} - {s.count(alpha)}")
