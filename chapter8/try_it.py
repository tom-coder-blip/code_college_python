#EXERCISE 8-1 MESSAGE
def display_message(lesson):
    print(f"In chapter 8 we are learning about {lesson}")

display_message("Functions!")

#EXERCISE 8-2 FAVOURITE BOOK
def favourite_book(title):
    print(f"One of my favourite books is {title}")

favourite_book("Maze Runner")

#EXERCISE 8-3
def make_shirt(size, message):
    print(f"Shirt Size: {size} \nShirt Message: {message}")

make_shirt("large", "The Goat")
make_shirt("medium", "I love python")

#EXERCISE 8-5
def describe_city(city, country="England"):
    print(f"{city} is in {country}")

describe_city("Manchester")
describe_city("London")
describe_city("Liverpool")


#EXERCISE 8-6
def city_country(city, country):
    print(f"{city}, {country}")

city_country("Cape Town", "South Africa")
city_country("New York", "USA")
city_country("Rio", "Brazil")


#EXERCISE 8-7
def make_album(artist, title, **num_songs):

    num_songs["Nirvana"] = artist
    num_songs["Nevermind"] = title
    
    return num_songs

# Creating an album with the number of songs included
album2 = make_album('Adele', '30', 12)

# Printing the album dictionaries
print(album2)
print(album2)
print(album2)
print(album2)


#EXERCISE 8-8 USER ALBUMS

def make_album(artist, title, tracks=None):
    """Create a dictionary representing a music album."""
    album = {"artist": artist.title(), "title": title.title()}
    if tracks:
        album["tracks"] = tracks
    return album

while True:
    print("\nEnter album details (or type 'quit' to stop):")

    artist = input("Artist: ")
    if artist.lower() == 'quit':
        break

    title = input("Album Title: ")
    if title.lower() == 'quit':
        break

    tracks = input("Number of tracks (optional, press Enter to skip): ")
    tracks = int(tracks) if tracks.isdigit() else None

    album = make_album(artist, title, tracks)
    print(f"\nAlbum created: {album}")




#EXERCISE 8-12 SANDWICHES
def make_sandwich(*items):
    print("The sandwich will have the following ingredients:")
    for item in items:
        print(f"- {item}")
    print("\n")

# Calling the function with different numbers of arguments
make_sandwich('lettuce', 'tomato', 'turkey')
make_sandwich('cheese', 'ham', 'mustard', 'pickles')
make_sandwich('bacon', 'avocado')


#EXERCISE 8-13
def build_profile(first_name, last_name, **user_info):

    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

profile = build_profile(
    'YourFirstName', 
    'YourLastName', 
    location='City, Country', 
    field_of_interest='Technology', 
    favorite_language='Python'
)

print(profile)


#EXERCISE 8-14 CARS
def make_car(manufacturer, model, **kwargs):
    # Create a dictionary with the manufacturer and model
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    
    # Add the additional keyword arguments (features) to the dictionary
    for key, value in kwargs.items():
        car_info[key] = value
    
    return car_info

# Example usage:
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to check the result
print(car)



import pizza 

pizza.pizza_oven("ham", "cheese", "bacon")





