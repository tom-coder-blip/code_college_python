# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# glitchy = input("Fix this.")

# try:
#     print(glitchy)
# except:
#     print("No value passed yet...")
# else:
#     print("A value was passed...")


# #10-6
# def add_numbers():
#     try:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         result = num1 + num2
#         print(f"The sum is: {result}")

#     except ValueError:
#         print("Error: Please enter valid numbers only.")

# add_numbers()


#10-8 Modify your except block to fail silently if either file is missing
def add_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        pass  

add_numbers()



