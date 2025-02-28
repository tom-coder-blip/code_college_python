#1
def display_message(lesson):
    print(f"I am learning about {lesson}")

display_message("Functions")

#2
def favourite_book(title):
    print(f"One of my favourite books is {title}")

favourite_book("Maze runner")

#3
def make_shirt(size, message):
    print(f"Size of shirt: {size}\nMessage on shirt: {message}")

make_shirt("Large", "I am him")


#4
def make_shirt(message, size = "Large"):
    print(f"Size of shirt: {size} \nMessage on shirt: {message}")

make_shirt("I love python")


#5
def describe_city(city, country = "England"):
    for cities in city:
        print(f"{cities} is in {country}")

describe_city(["Manchester", "London", "Huddersfield"])


#6
#EXERCISE 8-6
def city_country(city, country):
    print(f"{city}, {country}")

city_country("Cape Town", "South Africa")
city_country("New York", "USA")
city_country("Rio", "Brazil")


#7
def make_album(artist, title, num_songs=None):
    # """Create a dictionary representing a music album."""
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album


album1 = make_album('Pink Floyd', 'The Dark Side of the Moon')
album2 = make_album('The Beatles', 'Abbey Road')
album3 = make_album('Nirvana', 'Nevermind')

album4 = make_album('Adele', '30', 12)
album4 = make_album('J', '40')

print(album1)
print(album2)
print(album3)
print(album4)


#9
def show_messages(messages):

    for message in messages:
        print(message)

text = [
    "Hello! How are you?",
    "Don't forget our meeting at 3 PM.",
    "Have a great day!",
    "See you soon!",
    "Call me when you're free."
]

# Call the function to display messages
show_messages(text)


#12
def make_sandwich(*items):
    print("The sandwich will have the following ingredients:")
    for item in items:
        print(f"- {item}")
    print("\n")

make_sandwich('lettuce', 'tomato', 'cheese')
make_sandwich('cheese', 'ham', 'mustard', 'bbq')
make_sandwich('bacon', 'avocado', 'mayo')


#13
def build_profile(first_name, last_name, **user_info):

    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

profile = build_profile(
    'Tom', 
    'Vuma', 
    location='Centurion, SA', 
    field_of_interest='Technology', 
    favorite_language='Python'
)

print(profile)


#14
def make_car(manufacturer, model, **kwargs):
    
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    
    for key, value in kwargs.items():
        car_info[key] = value
    
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)



