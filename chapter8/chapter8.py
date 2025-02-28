# my_name = input("May I have your name please: ")

# def my_function():
#     print(my_name)

# my_function()



def my_name(user, age, nation = ""):
    print(f"Welcome back {user}! It must be nice to be {age} years old.  A proud {nation}")

my_name( input("May I have your name please: "), input("How old are you: "), input("Where are you from: "))
my_name(input("May I have your name please: "), input("How old are you: "))



# def my_name(user, age, nation = "South African"):
#     print(f"Welcome back {user}! It must be nice to be {age} years old. A proud {nation}")

# my_name(user = input("May I have your name please: "), age = input("How old are you: "))
# my_name(user = input("May I have your name please: "), age = input("How old are you: "))



# def describe_city(city, country= "RSA"):
#     print(f"{city} is in {country}")
#     if city=="Pretoria":
#         return f"{city}, ooh so you use a Gautrain.."
#     elif city == "Jhb":
#         return f"{city}, have you seen Vilakazi street"
#     elif city == "Cpt":
#         return f"{city}, have you been to Camps bay"
#     elif city == "Kimberly":
#         return f"{city}, have you seen the big hole"
#     else:
#         return f"I don't know {city}"
    
# output = describe_city(input("Enter your city: "))
# print(output) 


# variable = True    #have to use if statement to escape the loop
# while variable:
#     print("Hey there")
#     variable = False

# print("Bye")



# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']

# greet_users(usernames[:])


# my_list = [1, 2, 3, 4, 5]

# def my_test_function():
#     list.reverse()
#     print(list)

# my_test_function(my_list[:])



# def welcome_people(names):

#     for name in names:
#         message = f"Welcome, {name}!"
#         print(message)
# usernames = ['John', 'Peter', 'Andrew']

# welcome_people(usernames)


def my_name(user, age, nation = ""):
    print(f"Welcome back {user}! It must be nice to be {age} years old.  A proud {nation}")

my_name( input("May I have your name please: "), input("How old are you: "), input("Where are you from: "))
my_name(input("May I have your name please: "), input("How old are you: "))


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')