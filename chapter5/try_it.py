#EXERCISE 5-3 ALIEN COLORS 1 
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")


#EXERCISE 5-4 ALIEN COLORS 2
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

else:
    print("You just earned 10 points!")


#EXERCISE 5-5 ALIEN COLORS 3
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


#EXERCISE 5-6 STAGES OF LIFE
age = 25 

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


#EXERCISE 5-7 FAVOURITE FRUIT
favorite_fruits = ["pineapple", "strawberry", "watermelon"]

# Checking for specific fruits in the list
if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "strawberry" in favorite_fruits:
    print("You really like strawberries!")

if "watermelon" in favorite_fruits:
    print("You really like watermelons!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "grapes" in favorite_fruits: 
    print("You really like grapes!")


#EXERCISE 5-8 HELLO ADMIN
usernames = ['admin', 'Jaden', 'Emily', 'John', 'Alice']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")


#EXERCISE 5-9 NO USERS
users = []

# Check if the list is empty
if not users:
    print("We need to find some users!")
else:
    # Greet each user in the list
    for user in users:
        print(f"Hello, {user}!")


# #EXERCISE 5-10 CHECKING USERNAMES
# current_users = ['alice', 'bob', 'charlie', 'dave', 'eve']

# new_users = ['alice', 'Frank', 'bob', 'Grace', 'Heidi']

# # Convert the current usernames to lowercase for case-insensitive comparison
# current_users_lower = [user.lower() for user in current_users]

# # Check if each new username is available
# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(f"Sorry, the username '{new_user}' has already been taken. Please choose a new one.")
#     else:
#         print(f"The username '{new_user}' is available.")


#EXERCISE 5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list
for number in numbers:
    # Use if-elif-else to determine the correct ordinal ending
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")



