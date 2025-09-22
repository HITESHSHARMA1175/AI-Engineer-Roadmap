# Day 2 exercises
# Topic: Month1_CoreFoundations / Week1_Python

# --- Topic: Lists (Mutable, Ordered) ---

print("--- Lists ---")
# create a list
course = ["history", "math", "phy", "comp"]

# by this we can print length
print(f"Length of course list: {len(course)}")

# by this we can acsses the list items
print(f"Full course list: {course}")

# by the index we can acces the spacific value of item
print(f"Element at index 1: {course[1]}")

# negative index in the case we don't know the last item of list we can find by -ve index it start from -1
print(f"Last element in list: {course[-1]}") #it is last item of list

# how to add item in list it will taken by append()
course.append("english")
print(f"List after appending 'english': {course}")

# by the help of insert() you choose a spacific location to add new item in list
course.insert(1, "art")
print(f"List after inserting 'art' at index 1: {course}")

# use of extend() it extend the list to add another element item
course2 = ['education', 'civics']
course.extend(course2)
print(f"List after extending with another list: {course}")

# by the remove() we can remove any item from the list
course.remove('math')
print(f"List after removing 'math': {course}")

# insted of remove() we can use pop()
# here intersting thing is that it remove elment from last and return the list
popped = course.pop()
print(f"The popped item was: '{popped}'")
print(f"List after pop(): {course}")

# here we can print reverse of any list by reverse()
course.reverse()
print(f"Reversed list: {course}")

# here by the help of sort() we can sort the list by alfaabetical order
course.sort()
print(f"Sorted list (alphabetical): {course}")

# sorting numbers
num = [1, 5, 6, 7, 9, 4]
# by this we can sort the list in reverse order
num.sort(reverse=True)
print(f"Numbers sorted in reverse: {num}")

# by this min() we can find the minimum element in the list
print(f"Min number in num list: {min(num)}")
# by the help of sum() we can print the sum of whole element in the list
print(f"Sum of num list: {sum(num)}")

# how to find the index of any element in the list
print(f"Index of 'phy': {course.index('phy')}")

# here by this we can cheak that elment is listed in list or not
print(f"Is 'history' in course list? {'history' in course}") #it will give true or false

# here by this method we can access the each element of the list
print("\nIterating through the list with a for loop:")
for item in course: #here item word is not any key word it caan be anything
    print(item)

# here by the help of enumerate() by using in tis method  we can print index also of each element
print("\nIterating with enumerate to get index and value:")
for index, h in enumerate(course):
    print(index, h)

# here by the help of start value we can modify our index starting
print("\nIterating with enumerate starting at 1:")
for index, h in enumerate(course, start=1):
    print(index, h)

# here by this we can modify the sepration it could be , - or anythin
course_str = ' - '.join(course)
print(f"\nList joined into a string: '{course_str}'")


# --- Topic: Tuples (Immutable, Ordered) ---
# it is quatly simler as list but it can't modify
# tuples are imutable(cont't cange) list are mutable(can change)
# here we use ( ) inted of []which is fot list
print("\n--- Tuples ---")
tuple_1 = ("history", "math", "english")
# tuple_1[0]="art" # This line would cause an error because tuples are immutable
print(f"My tuple: {tuple_1}")


# --- Topic: Sets (Mutable, Unordered, No Duplicates) ---
# sets are unordered collections of unique elements.
print("\n--- Sets ---")
cs = {"history", "math", "biology", "math"} # "math" is a duplicate, will be ignored
print(f"My set (duplicates removed): {cs}")


# --- Topic: Dictionaries (Mutable, Ordered, Key-Value Pairs) ---
print("\n--- Dictionaries ---")
# dictionary is a built-in data structure that stores data in key-value pairs.
student = {'name': 'Hitesh', 'age': 22, 'phone': '134526'}
print(f"Original dictionary: {student}")

# we can update by update()
student.update({'name': 'Hitesh Sharma', 'age': 23, 'courses': ['AI', 'ML']})
print(f"Updated dictionary: {student}")

# remove a key and get its value
age = student.pop('age')
print(f"Popped age: {age}")
print(f"Dictionary after popping age: {student}")

# for printin keys only
print(f"Keys: {student.keys()}")
# for printing values only
print(f"Values: {student.values()}")
# it will print all the item in the dict key and values all
print(f"Items: {student.items()}")

# here for printing each key and value saprated
print("\nIterating through dictionary items:")
for key, value in student.items():
    print(f"{key}: {value}")
