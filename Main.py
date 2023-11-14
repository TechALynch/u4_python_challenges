# Python Challenges

#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
def minutes_to_seconds(minutes):
    return minutes * 60

minutes = 1
seconds = minutes_to_seconds(minutes)
print(f"{minutes} minutes is equal to {seconds} seconds.")

# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
def hours_to_seconds(hours):
    return hours * 60 * 60

hours = 1
seconds = hours_to_seconds(hours)
print(f"{hours} hours is equal to {seconds} seconds.")

# -  We're on the right track here, how many seconds are in a day
def day_to_seconds(day):
    return day * 60 * 60 * 24

day = 1
seconds = day_to_seconds(day)
print(f"{day} day(s) is equal to {seconds} seconds.")

# - How many Hours are in the month of June? ##30 days in june
def june_to_hours(june):
    return june * 24 * 30

june = 1
hours = june_to_hours(june)
print(f"{june} june(s) is equal to {hours} hours.")

# - How many Minutes are in the month of August?
def august_to_minutes(august):
    return august * 24 * 60 * 31

august = 1
minutes = august_to_minutes(august)
print(f"{august} August(s) is equal to {minutes} minutes.")
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?

# ---------------------------------
minutes_in_a_day = 24 * 60
days_in_a_year = 365
days_in_a_leap_year = 366
minutes_in_a_year = days_in_a_year * minutes_in_a_day
minutes_in_a_week = 7 * minutes_in_a_day
cups_per_day = .5
cups_in_a_year = cups_per_day * days_in_a_year

print(f"Minutes in a day: {minutes_in_a_day}")
print(f"Minutes in a year (ordinary): {minutes_in_a_year}")
print(f"Minutes in a week: {minutes_in_a_week}")
print(f"Cups of coffee in a year: {cups_in_a_year}")
# ---------------------------------

#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
def mid(string):
    length = len(string)

    if length % 2 == 0 or length == 0:
        return ""
    else:
        middle_index = length // 2
        return string[middle_index]

# Test cases
print(mid("abc")) 
print(mid("aaaa"))   
print(mid("python")) 
print(mid("pythonn")) 

# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
def hide_last4_num(credit_card_num):
    hidden_part = '*' * (len(credit_card_num) - 4)
    visible_part = credit_card_num[-4:]
    hide_card_return = hidden_part + visible_part
    return hide_card_return

my_card = "1234567894444"
print(hide_last4_num(my_card))
# ---------------------------------

# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

def online_count(statuses):
    online_people_values = sum(status == "online" for status in statuses.values())
    return online_people_values

online_people = online_count(statuses)
print(online_people)

# ---------------------------------

#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
def item(price, discount):
    total = price - discount
    return total
print(item(100, 20))
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse

# ---------------------------------

# need to import math
import math
def calculate_hypotenuse(adjacent, opposite):
    # Pythagorean theorem formula = legs Squared, add them together, then take the square root of that value
    adjacent_squared = adjacent ** 2
    opposite_squared = opposite ** 2
    hypotenuse_squared = adjacent_squared + opposite_squared
    hypotenuse = math.sqrt(hypotenuse_squared)
    return hypotenuse

adjacent_leg = 3
opposite_leg = 4
hypotenuse_answer = calculate_hypotenuse(adjacent_leg, opposite_leg)
print(hypotenuse_answer)

# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
def fibonacci_sequence(num1, num2):
    sequence = [num1, num2]

    for i in range(9):
        next_fnumber = sequence[-1] + sequence[-2]
        sequence.append(next_fnumber)

    return sequence

initial_num1 = 0
initial_num2 = 1
next9_fibonacci_sequence_num = fibonacci_sequence(initial_num1, initial_num2)
print(next9_fibonacci_sequence_num)

# ---------------------------------
