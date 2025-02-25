# # Creating a list of favorite movies
# favourite_movies = ["return of the King", "matrix: Reloaded", "philosopher's Stone"]

# # Looping through the list and printing each movie title
# for movie in favourite_movies:
#     print(f"This is one of my favourite movies {movie}")

# # Looping through the list again, formatting the titles properly, and printing them
# for movie in favourite_movies:
#     proper_title = movie.title()  # Converts each movie title to title case
#     print(f"This is one of my favourite movies {proper_title}")

# # Using range() to print numbers from 3 to 19 (range excludes the upper limit)
# for number in range(3, 20):
#     print(number)

# # Creating a range of numbers from 1 to 19
# my_numbers = range(1, 20)
# empty_list = []  # Initializing an empty list

# # Looping through my_numbers and adding each number to empty_list
# for number in my_numbers:
#     empty_list.append(number)

# # Printing the populated list
# print(empty_list)

# # Slicing the first two elements from the favourite_movies list and printing them
# print(favourite_movies[0:2])  

# # Creating a list of favorite ice cream flavors
# favourite_icecream = ["Vanilla", "Choc", "Blueberry", "Caramel"]

# # Slicing and printing the second and third elements from the favourite_icecream list
# print(favourite_icecream[1:3])  


# my_tuple = (1, 2, 3, 4, 5)

# print(my_tuple[1])
# print(my_tuple[0:3])



# devices  = ["Laptop", "TV", "Speaker", "PC"]
# names = ("James", "Peter", "Andrew", "Simon")

# devices.insert(2, 66)
# print (devices)



#Exercise 4.1 PIZZAS
favorite_pizzas = ["pepperoni", "margherita", "hawaiian", "Bacon", "Pinapple", ]
for pizza in favorite_pizzas:
    print(f"I enjoy {pizza} pizza.")

print("Pizza all day makes me happy!")


#Exercise 4.2 animals
animals = ["lion", "cheetah", "leopard"]
for animal in animals:
      print(f"A {animal} would make a crazy pet.")

print("Any of these animals would make be wild!")


#Exercise 4.3 FOR LOOP COUNT TO 20
for number in range(1, 21):
    print(number)


#Exercise 4.10 SLICES
print("\nThe first three items in the list are: ")

print("The first three items in the list are:")
print(favorite_pizzas[0:3])


#Exercise 4.11

favorite_pizzas = ["pepperoni", "margherita", "hawaiian", "bacon", "pineapple"]

for pizza in favorite_pizzas:
    print(f"I enjoy {pizza} pizza.")

print("Pizza all day makes me happy!\n")

friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("BBQ Chicken")

friend_pizzas.append("Veggie Supreme")

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


#Exercise 4.13

buffet_menu = ("Rice", "Grilled Chicken", "Salad", "Soup", "Pasta")

print("The restaurant offers:")
for food in buffet_menu:
    print(food)

buffet_menu[1] = "Steak" 

buffet_menu = ("Rice", "Grilled Fish", "Salad", "Steak", "Noodles")

print("\nThe new restaurant menu:")
for food in buffet_menu:
    print(food) 