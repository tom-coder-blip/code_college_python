#1
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"The {self.restaurant_name} has {self.cuisine_type} as the best food")

    def open_restaurant(self):

        print(f"{self.restaurant_name} is now open.")


my_restaurant = Restaurant('Toms Tacos', 'Fancy Tacos')
your_restaurant = Restaurant('Jacks Burgers', 'Spanish Burgers')

print(f"{my_restaurant.restaurant_name} is a too nice.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"{your_restaurant.restaurant_name}is too nice.")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()



#3

class User:

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name: {self.first_name}\nLast_name: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. Its a pleasure to speak to you.")


user_one = User('John', 'Mahlangu')
user_two = User('Peter', 'Farreira')
user_three = User('Moses', 'Duma')

print(f"The first on the list: {user_one.first_name}. With an awesome surname {user_one.last_name}!")
user_one.describe_user()
user_one.greet_user()


print(f"The second on the list: {user_two.first_name}. With an awesome surname {user_two.last_name}!")
user_two.describe_user()
user_two.greet_user()

print(f"The third on the list: {user_three.first_name}. With an awesome surname {user_three.last_name}!")
user_three.describe_user()
user_three.greet_user()


#4
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        print(f"The {self.restaurant_name} has {self.cuisine_type} as the best food")


    def open_restaurant(self):

        print(f"{self.restaurant_name} is now open.")


    def set_number_served(self, number):
        #Sets the number of customers served to a specific value.
        if number >= 0:
            self.number_served = number
        else:
            print("Number of customers served cannot be negative.")


    def increment_number_served(self, number):
        #Increments the number of customers served by a given amount.
        if number > 0:
            self.number_served += number
        else:
            print("Increment value must be positive.")


my_restaurant = Restaurant('Toms Tacos', 'Fancy Tacos')
your_restaurant = Restaurant('Jacks Burgers', 'Spanish Burgers')
restaurant = Restaurant("Toms Tacos", "Fancy Tacos")


print(f"{my_restaurant.restaurant_name} is a too nice.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"{your_restaurant.restaurant_name}is too nice.")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()


# Printing default number of customers served
print(f"Customers served: {restaurant.number_served}")

# Changing and printing the number of customers served
restaurant.set_number_served(50)
print(f"Customers served after update: {restaurant.number_served}")

# Incrementing the number of customers served
restaurant.increment_number_served(30)
print(f"Customers served after increment: {restaurant.number_served}")


#5
class User:

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}\nLast_name: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. Its a pleasure to speak to you.")

    def increment_login_attempts(self):
        #Increments the login_attempts by 1
        self.login_attempts += 2

    def reset_login_attempts(self):
        #Resets login_attempts to 0.
        self.login_attempts = 0


user_one = User('John', 'Mahlangu')
user_two = User('Peter', 'Farreira')
user_three = User('Moses', 'Duma')

print(f"The first on the list: {user_one.first_name}. With an awesome surname {user_one.last_name}!")
user_one.describe_user()
user_one.greet_user()
# Calling increment_login_attempts() multiple times
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
# Printing login attempts to ensure it was incremented properly
print(f"Login attempts: {user_one.login_attempts}")
# Resetting login attempts
user_one.reset_login_attempts()
# Printing login attempts after reset
print(f"Login attempts after reset: {user_one.login_attempts}")


print(f"The second on the list: {user_two.first_name}. With an awesome surname {user_two.last_name}!")
user_two.describe_user()
user_two.greet_user()
# Calling increment_login_attempts() multiple times
user_two.increment_login_attempts()
# Printing login attempts to ensure it was incremented properly
print(f"Login attempts: {user_two.login_attempts}")
# Resetting login attempts
user_two.reset_login_attempts()
# Printing login attempts after reset
print(f"Login attempts after reset: {user_two.login_attempts}")


print(f"The third on the list: {user_three.first_name}. With an awesome surname {user_three.last_name}!")
user_three.describe_user()
user_three.greet_user()
# Calling increment_login_attempts() multiple times
user_three.increment_login_attempts()
# Printing login attempts to ensure it was incremented properly
print(f"Login attempts: {user_three.login_attempts}")
# Resetting login attempts
user_three.reset_login_attempts()
# Printing login attempts after reset
print(f"Login attempts after reset: {user_three.login_attempts}")





#6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} has {self.cuisine_type} as the best food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors  # List of ice cream flavors

    def display_flavors(self):
        """Displays the available ice cream flavors."""
        print(f"{self.restaurant_name} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint"])

# Calling the method to display flavors
ice_cream_stand.display_flavors()




class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")

    def honk(self):
        print(f"{self.brand} {self.model} says: Beep! Beep!")

my_car = Car("Toyota", "Corolla", 2022)

my_car.display_info()
my_car.honk()
print(f"{my_car.brand} is a my favourote!")




class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is not an adult")

person1 = Person("Alice", 25)

person1.display_info()
person1.is_adult()



class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Book title: {self.title}\nBook Author: {self.author}\nYear published: {self.year}")

    def is_old(self):
        if self.year < 2000:
            print(f"{self.title} is an old book.")
        else:
            print(f"{self.title} is a relative new book.")


my_book = Book("The Great Gatsby", "F. SCott Fitzgerald", 1935)
my_book.display_info()
my_book.is_old