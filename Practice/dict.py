# data = {
#     "name": "Alice",
#     "age" : 25,
#     "city": "New York",
#     "occupation": "Software Developer"
    
# }

# key = input("Enter a key(name, age, city, occupation): ").strip()

# if key in data:
#     print(f"The value for '{key}' is: {data[key]}")
# else:
#     print("Key not found in dictionary.")


# country_capitals = {
#     "USA": "Washington, D.C.",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "India": "New Dehli",
#     "Germany": "Berlin"
# }

# country = input("Enter a country name to get its capital: ").strip()

# capital = country_capitals.get(country)

# if capital:
#     print(f"The capital of {country} is {capital}.")
# else:
#     print("Country not found in the dictionary.")


# student_scores = {
#     "Jack" : 85,
#     "Charls" : 78,
#     "Candace" : 99,
#     "Bobby" : 90
# }

# name = input("Enter a student's name to get their score: ")

# if name in student_scores:
#     print(f"{name}'s score is {student_scores[name]}.")
# else:
#     print("Student not found in the records") 


capitals = {
    "USA" : "Washington , D.C",
    "France" : "Paris",
    "Germany" : "Berlin",
    "Japan" : "Tokyo",
    "India" : "New Delhi"
}

country = input("Enter a county name to get its capital: ")

if country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")
else:
    print("Country not found in the records.")


