# Day 5 exercises
# Topic: Month1_CoreFoundations / Week1_Python

# --- Part 1: Exploring Modules from the Python Standard Library ---
print("--- 1. Using Standard Library Modules ---")

import datetime
import calendar
import os
import webbrowser

# Using the datetime module
today = datetime.date.today()
print(f"Today's date is: {today}")

# Using the calendar module
is_2020_leap = calendar.isleap(2020)
print(f"Was 2020 a leap year? {is_2020_leap}")

# Using the os module
current_directory = os.getcwd()
print(f"This script is running from: {current_directory}")


# --- Part 2: Creating and Using a Custom Module ---
# In a real project, the function below would be in a separate file
# (e.g., 'my_module.py'), and we would import it from there.

print("\n--- 2. Defining a function for a custom module ---")

def find_index(search_list, target):
    """Finds the index of a target value in a list."""
    for i, value in enumerate(search_list):
        if value == target:
            return i
    return -1

# Now, let's pretend we are in a DIFFERENT file and we are importing the function above.
# This simulates how you would use your own module.
courses = ['History', 'Math', 'Physics', 'CompSci']
target_course = 'Physics'

# We call the function we defined earlier
index = find_index(courses, target_course)
print(f"The index of '{target_course}' is: {index}")


# --- Part 3: Other Explored Modules ---
print("\n--- 3. Other Explored Modules ---")
# The following line is commented out so it doesn't open a new tab every time.
# You can uncomment it to test it!
# webbrowser.open("https://xkcd.com/353/")
print("Explored the 'webbrowser' module to open websites.")

# You also correctly identified how to add a new folder to Python's path
# so it can find your modules. This is a key advanced concept!
# import sys
# sys.path.append('/path/to/your/modules')
print("Learned about 'sys.path' for managing module locations.")

