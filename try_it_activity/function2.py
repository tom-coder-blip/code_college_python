def favourite_language(fav_lang):
    print(f"My favourite lnguage is {fav_lang}!")

favourite_language("Python")


def daily_motivation(message):
    print(f"Good Morning champ! {message}. Have a solid day")

daily_motivation("Keep grinding and remember always that you are a Top G")


def favourite_hobby(hobby):
    print(f"My favourite hobby is {hobby}")

favourite_hobby("Football")


def favourite_book(title, author):
    print(f"Mt favourite book is {title} by {author}.")

favourite_book("Lets get it", "Jack Peterson")


def sum_numbers(*number):
    total = sum(number)
    print(f"The sum of the numbers is {total}.")

sum_numbers(5, 10, 15)



def build_student_record(first_name, last_name, **student_info):
    student_record = {}
    student_record['first_name'] = first_name
    student_record['last_name'] = last_name

    for key, value in student_info.items():
        student_record[key] = value
    
    return student_record

student = build_student_record(
    'Emily',
    'Smith',
    grade = '10th Grade',
    subjects = ['Math', 'Science', 'History'],
    extracurricular = 'Basketball'
)

print(student)



def build_employee_record(first_name, last_name, **emp_details):
    emp_info = {}
    emp_info['first_name'] = first_name
    emp_info['last_name'] = last_name
    
    for key, value in emp_details.items():
        emp_info[key] = value

    return emp_info

employee = build_employee_record(
    'Jack',
    'Peterson',
    position = 'Project Manager',
    department = 'Data Analytics',
    salary = 'R80 000',
    years_of_exp = '16'

)

print(employee)



def build_car_info(brand, model, **car_details):
    car_info = {}
    car_info['brand'] = brand
    car_info['model'] = model

    for key, value in car_details.items():
        car_info[key] = value

    return car_info

car = build_car_info(
    'Hundai',
    'i20',
    year = '2015',
    color = 'Blue',
    fuel_type = 'Diesel'

)

print(car)



def build_book_info(book_title, author, **book_details):
    book_info = {}
    book_info['book_title'] = book_title
    book_info['author'] = author

    for key, value in book_details.items():
        book_info[key] = value

    return book_info
    
book = build_book_info(
    'Run Run Run',
    'Peter Jackson',
    genre = 'Action',
    pub_year = '2014'

)

print(book)



trip_info = {}

def plan_trip(**trip_details):

    for key, value in trip_details.items():
        trip_info[key] = value

    return trip_info
    
plan = plan_trip(
    country = "Greece",
    destination = "Santorini",
    budget = 10000

)

print(plan)


def make_pizza(*toppings):
    print("The pizza will have the following toppings: ")
    for toppings in toppings:
        print(f"{toppings}")

make_pizza('pepperoni', 'mushrooms', 'cheese')
make_pizza('onions', 'green peppers', 'extra cheese')
make_pizza('bacon', 'pineapple', 'extra cheese')



def create_pet_profile(pet_name, pet_type, **pet_info):
    pet_details = {}
    pet_details['pet_name'] = pet_name
    pet_details['pet_type'] = pet_type

    for key, value in pet_info.items():
        pet_details[key] = value

    return pet_details

pet = create_pet_profile(
    'Bobby',
    'Dog',
    breed = 'Ridgeback',
    age = '7',
    kids = '1'

)

print(pet)



def create_travel_profile(traveler_name, destination, **travel_info):
    travel_details = {}
    travel_details['traveler_name'] = traveler_name
    travel_details['destination'] = destination

    for key, value in travel_info.items():
        travel_details[key] = value

    return travel_details

travel = create_travel_profile(
    'Jack',
    'Greece',
    city = 'Santorini',
    budget = '10000',
    accomodation = 'hotel'

)

print(travel)