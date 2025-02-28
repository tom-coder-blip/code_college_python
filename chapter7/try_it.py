#EXERCISE 7-1 RENTAL CAR
# car_preference = input("What kind of rental car would you like? ")

# print(f"Let me see if I can find you a {car_preference}.")


# #EXERCISE 7-2 RESTUARANT SEATING 
# num_people = int(input("How many people are in your dinner group? "))

# # Check if the group size is more than 8
# if num_people > 8:
#     print("Sorry, you'll have to wait for a table.")
# else:
#     print("Your table is ready!")


# #EXERCISE 7-3 MULTIPLES OF TEN
# number = int(input("Enter a number: "))

# # Check if it's a multiple of 10
# if number % 10 == 0:
#     print(f"{number} is a multiple of 10.")
# else:
#     print(f"{number} is not a multiple of 10.")


#EXERCISE 7.5 MOVIE TICKETS
while True:
    age = input("Enter your age (or type 'quit' to exit): ")
    if age.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break
    
    if age.isdigit(): 
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
    else:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")


#EXERCISE 7-6 THREE EXISTS
prompt = "Enter your favorite city (or type 'quit' to exit): "

city = input(prompt)
while city.lower() != 'quit':
    print(f"{city} sounds like a great place!")
    city = input(prompt)

print("Goodbye!")


#EXERCISE 7-7 INFINITY LOOP
# while True:
#     print("This loop will run forever! Press CTRL-C to stop.")


#EXERCISE 7-8 DELI
sandwich_orders = ["tuna", "ham and cheese", "chicken", "veggie", "turkey"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Remove the first sandwich from the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)  # Move it to the finished list

# Print all finished sandwiches
print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")


#EXERCISE 7-10 DREAM VACATION
def dream_vacation_poll():
    responses = {}
    
    while True:
        name = input("What is your name? ")
        destination = input("If you could visit one place in the world, where would you go? ")
        
        responses[name] = destination
        
        repeat = input("Would you like to let another person respond? (yes/no) ")
        
        if repeat.lower() != 'yes':
            break
    
    print("\n--- Poll Results ---")
    for name, destination in responses.items():
        print(f"{name} would like to visit {destination}.")

# Run the poll
dream_vacation_poll()