#1
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
       
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("The Food Haven", "Italian")

# Printing attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()


#2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant name and cuisine type."""
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} cuisine.\n")

restaurant1 = Restaurant("Ocean Baskets", "Seafood")
restaurant2 = Restaurant("Cuurry Kings", "Indian")
restaurant3 = Restaurant("Pizza Italia", "Italian")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

