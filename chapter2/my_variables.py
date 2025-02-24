# Defining variables for a name, surname, and a sentence
name = "harry"
surname = "Maguire"
sentence = "The best baller alive!"

# Using an f-string to concatenate and format the final display string
final_display = f"{name} {surname} {sentence}"

# Printing the final display string with a tab space at the beginning
print(f"\t{final_display}")

# Printing a multiline formatted message with tab spaces and newline characters
print(f"\tHello there,\n\tWelcome to my house.\n\tLet me offer you a hot beverage.\nMake yourself comfortable and feel free to watch some TV. ")

# Printing a table-like format with tab spacing for alignment
print("Name\tAge\tCountry")
print("Tom\t21\tSouth Africa")

# Using the lstrip() method to remove leading spaces in the string
print("           Tom".lstrip())

# Defining a URL string
mylink = "https://classroom.google.com/"

# Using removeprefix() to remove the "https://" part from the URL
print(mylink.removeprefix("https://"))

# Defining multiple variables in a single line
name, surname, age, gender = "Jack", "Peterson", 55, "Male"

# Printing the values of name and age
print(name)
print(age)

# Importing the "this" module, which prints "The Zen of Python" by Tim Peters
import this  

# Using the title() method to capitalize the first letter of each word in "name"
print(name.title())  
