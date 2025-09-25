# Day 4 exercises
# Topic: Month1_CoreFoundations / Week1_Python

print("--- Basic Functions ---")

# A simple function that just performs an action (prints)
def hello_func_action():
    """Defines a function that prints a greeting."""
    print("Hello, this function just prints a message.")

# Calling the function to perform its action
hello_func_action()

# A function that returns a value
def hello_func_return():
    """Defines a function that returns a string value."""
    return 'Hello, this function returns a value.'

# Calling the function and printing the returned value
returned_value = hello_func_return()
print(returned_value)


print("\n--- Functions with Arguments ---")

# A function that accepts a required argument
def greet(greeting):
    """Takes a greeting and formats it into a string."""
    return '{} function.'.format(greeting)

print(greet('Hi'))

# A function with a required argument and an optional (default) argument
def greet_with_name(greeting, name='You'):
    """Takes a greeting and an optional name."""
    return '{}, {}!'.format(greeting, name)

print(greet_with_name('Hi')) # Uses the default name
print(greet_with_name('Hi', name='Hitesh')) # Overrides the default


print("\n--- Practical Example: Leap Year Calculator ---")

# This is a great example of functions working together.
# One function helps another one do its job.

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """
    Determines if a given year is a leap year.
    Returns True for a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """
    Calculates the number of days in a given month of a specific year,
    accounting for leap years.
    """
    # First, check for invalid input
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    # Check for February in a leap year
    if month == 2 and is_leap(year):
        return 29
    
    # Return the number of days from the list
    return month_days[month]

# --- Testing the Leap Year Functions ---
year_to_check = 2020
month_to_check = 2
print(f"Is the year {year_to_check} a leap year? {is_leap(year_to_check)}")
print(f"Days in month {month_to_check} of {year_to_check}: {days_in_month(year_to_check, month_to_check)}")

year_to_check = 2019
print(f"Days in month {month_to_check} of {year_to_check}: {days_in_month(year_to_check, month_to_check)}")

