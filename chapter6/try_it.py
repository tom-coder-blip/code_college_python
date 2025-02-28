#EXERCISE 6-1 PERSON
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}

# Printing each piece of information
print("First Name:", person["first_name"])
print("Last Name:", person["last_name"])
print("Age:", person["age"])
print("City:", person["city"])


#EXERCISE 6-2 FAVOURITE NUMBERS
favorite_numbers = {
    "James": 7,
    "John": 14,
    "Simon": 3,
    "Andrew": 21,
    "Jack": 9
}

# Printing each person's favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")


#EXERCISE 6-3 GLOSSARY
glossary = {
    "Variable": "A named storage location in memory that holds a value.",
    "Function": "A block of reusable code that performs a specific task.",
    "Loop": "A control structure that repeats a block of code multiple times.",
    "List": "A collection of ordered items that can be changed (mutable).",
    "Dictionary": "A collection of key-value pairs used for fast data retrieval."
}

# Print the glossary in a formatted way
for word, meaning in glossary.items():
        print(f"{word}:\n  {meaning}\n")


#EXERCISE 6-4 GLOSSARY 2
glossary["tuple"] = "An immutable ordered collection of items in Python."
glossary["set"] = "An unordered collection of unique items in Python."
glossary["module"] = "A file containing Python code that can be imported into another program."
glossary["class"] = "A blueprint for creating objects in object-oriented programming."
glossary["object"] = "An instance of a class that contains attributes and methods."

# Loop through the dictionary and print each term with its definition
print("Python Glossary:")
for term, meaning in glossary.items():
    print(f"\n{term.title()}:\n  {meaning}")


#EXERCISE 6-5 RIVERS 
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Printing a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Printing the name of each river
print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(river)

# Printing the name of each country
print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country)


#EXERCISE 6-6 POLLING
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'philly': 'python',
}

# List of people who should take the poll
people_to_poll = ['jen', 'sarah', 'mike', 'anna', 'philly', 'tom']

# Loop through the list and check if they have taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, we invite you to take the favorite languages poll!")


#EXERCISE 6-7 PEOPLE
person_1 = {
    'first_name': 'John',
    'last_name': 'Black',
    'age': 28,
    'city': 'Pretoria'
}

person_2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 34,
    'city': 'Joburg'
}

person_3 = {
    'first_name': 'Peter',
    'last_name': 'Johnson',
    'age': 24,
    'city': 'Cape Town'
}

# Storing all dictionaries in a list
people = [person_1, person_2, person_3]

# Looping through the list and printing details about each person
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()



#EXERCISE 6-8 PETS
pet1 = {'animal': 'dog', 'owner': 'Alice'}
pet2 = {'animal': 'cat', 'owner': 'Bob'}
pet3 = {'animal': 'rabbit', 'owner': 'Charlie'}

# Storing the dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Looping through the list and printing details about each pet
for pet in pets:
    print(f"Animal: {pet['animal']}, Owner: {pet['owner']}")


#EXERCISE 6-9 FAVORITE PLACES
favorite_places = {
    'Alice': ['Paris', 'New York', 'Tokyo'],
    'Bob': ['Sydney', 'London'],
    'Charlie': ['Rome', 'Berlin', 'Cape Town', 'Madrid']
}
#I didnt create the loop yet


#EXERCISE 6-11
cities = {
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'Known as the "Big Apple" and is a global financial hub.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous metropolitan area in the world.'
    },
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'Home to the iconic Eiffel Tower and rich cultural history.'
    }
}

# Printing the information for each city
for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")



car_1 = {
    "brand": "Toyota",
    "model" : "Corolla",
    "year": 2020,
    "color": "Blue"
}

car_2 = {
    "brand": "Honda",
    "model": "Civic",
    "year": "2018",
    "color": "Red"
}

car_3 = {
    "brand": "Ford",
    "model": "Civic",
    "year": 2018,
    "color": "Red"
}

cars = [car_1, car_2, car_3]

for car in cars:
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Year: {car['year']}")
    print(f"Color: {car['color']}")
    print()
