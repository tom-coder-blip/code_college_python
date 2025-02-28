def pizza_oven(*toppings):
    if not toppings:
        print("You didn't add any toppings. Here's a plain pizza.")
    else:
        print("Here are the toppings for your pizza:")
        for topping in toppings:
            print(f"{topping}")
        print(f"\nTotal toppings: {len(toppings)}")

# Example usage
pizza_oven("Ham", "Cheese", "Pepper")
pizza_oven()  # No toppings




# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     if not toppings:
#         print("- Plain cheese")
#     else:
#         for topping in toppings:
#             print(f"- {topping}")
#     print("Your pizza will be ready shortly. Thank you for your order!")

# print("Welcome to Python Pizza!")
# make_pizza(input("What size pizza do you want?"), input("What toppings would you like?"))
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# make_pizza(18)
# print("We hope you enjoy your meal!")


def test(first, *second):
    print(f"this is my first argument: {first}")
    print(f"these are my other argumenents: {second}")

    test(1, 2, 3, 4, second = 5)

def pizza_fail(customer):
    print(f"{customer}'s ")


