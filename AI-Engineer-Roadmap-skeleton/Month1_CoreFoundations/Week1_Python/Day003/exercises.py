# Day 3 exercises
# Topic: Month1_CoreFoundations / Week1_Python

print("--- Conditional Statements ---")

# if, elif, else statement
lng = "Java"
print(f"Checking language: {lng}")
if lng == "python":
    print("Condition is Python")
elif lng == "Java":
    print("Condition is Java")
else:
    print("No condition met")

# Logical 'and' operator
user = "admin"
logged_in = True
print(f"\nUser is '{user}' and logged_in is {logged_in}")
if user == "admin" and logged_in:
    print("Admin access granted")
else:
    print("Access denied")

# How Python evaluates different values (truthiness)
print("\n--- Evaluating Truthiness ---")
# False values: None, False, 0, empty sequences/collections
false_conditions = [False, None, 0, '', [], {}, ()]
for condition in false_conditions:
    if condition:
        print(f"{condition} evaluated to True")
    else:
        print(f"'{condition}' evaluated to False")

# True values: any non-empty collection or non-zero number
true_conditions = [True, 10, 'hello', [1, 2]]
for condition in true_conditions:
    if condition:
        print(f"'{condition}' evaluated to True")
    else:
        print(f"{condition} evaluated to False")


print("\n--- Loops ---")

# --- For Loops ---
print("\n--- For Loop with break ---")
# break statement stops the loop entirely
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    if num == 4:
        print("Found 4, breaking loop!")
        break
    print(num)

print("\n--- For Loop with continue ---")
# continue statement skips the rest of the current iteration and moves to the next
for num in nums:
    if num == 3:
        print("Found 3, skipping to next iteration...")
        continue
    print(num)

print("\n--- Nested For Loop ---")
for num in [1, 2]:
    for letter in 'abc':
        print(num, letter)

# --- While Loops ---
print("\n--- While Loop with break ---")
x = 0
while x < 10:
    if x == 5:
        print("x is 5, breaking loop!")
        break
    print(x)
    x += 1

# --- Practical Example with User Input ---
# This part is commented out so the script can run without stopping for input.
# You can uncomment it to test the odd/even checker!
#
# print("\n--- Odd/Even Number Checker ---")
# num_input = input("Enter a number: ")
# if num_input: # check if user entered something
#     num = int(num_input)
#     if num % 2 == 0:
#         print(f"{num} is an Even number")
#     else:
#         print(f"{num} is an Odd number")

# --- Operators ---
print("\n--- Comparison Operators ---")
print(f"Is 4 == 4? {4 == 4}")
print(f"Is 4 != 4? {4 != 4}")
print(f"Is 4 > 2? {4 > 2}")

