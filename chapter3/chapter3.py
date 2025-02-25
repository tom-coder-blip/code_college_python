# # Define a list of classmates
# classmates = ["Aidan", "Asanda", "Cadee", "Courtney", "Ethan", "Lindo", "Phomello", "Ronny", "Sibu", "Tom", "Ulrich", "Mieke"]

# # Print the first classmate in the list (index 0)
# print(classmates[0])

# # Define a list with three items
# my_list = ["item1", "item2", "item3"]

# # Print the first item in my_list, formatted with title casing (first letter of each word capitalized)
# print(my_list[0].title())

# # Print the last item in my_list using negative indexing
# print(my_list[-1])

# # Append "Moses" to the end of my_list
# my_list.append("Moses")

# # Append the number 700 to the end of my_list
# my_list.append(700)

# # Insert the string "Vamos" at index 13 in my_list
# # Note: If the index is out of range, it will simply append it to the end
# my_list.insert(13, "Vamos")

# # Print the classmates list to show it remains unchanged
# print(classmates)

# # Delete the first element (index 0) from my_list
# del my_list[0]

# # Pop (remove and return) the last element from my_list and store it in number_4
# number_4 = my_list.pop()

# # Print the updated my_list after deletion and pop
# print(my_list)

# # Print the value that was popped from the list (stored in number_4)
# print(number_4)

# # Pop (remove and return) the element at index 1 and store it in item2
# item2 = my_list.pop(1)

# # Define a new list of numbers
# new_list = [1, 2, 3, 4, 5]

# # Remove the element at index 2 (third element) from new_list using pop()
# new_list.pop(2)

# # Remove the element with the value 4 from new_list using remove()
# new_list.remove(4)

# # Print the updated new_list
# print(new_list)

# # Define a list of letters
# alphabetical_list = ["b", "a", "c"]

# # Sort the alphabetical_list in ascending (alphabetical) order
# alphabetical_list.sort()

# # Print the sorted alphabetical_list
# print(alphabetical_list)



#Exercise 3.1 NAMES
names = ["Jack", "Bob", "Tim", "Brian"]
for name in names:
    print(name)


#Exercise 3.2 GREETINGS
names = ["Jack", "Bob", "Tim", "Brian"]
for name in names:
    print(f"Hello {name}. Welcome to my running club!")


#Exercise 3.3 YOUR OWN LIST
transport = ["Car", "Bike", "Uber", "Gautrain", "Bus"]
for trans in transport:
    print(f"I would like to buy my first {trans}. I cant wait to buy it!")


#Exercise 3.4 GUEST LIST
guest_list = ["Peter", "James", "Andrew", "John"]
for guest in guest_list:
    print(f"Dear {guest},\nYou are invited to join me for dinner. I look forward to seeing you!\n")


#Exercise 3.5 CHANGING THE GUEST LIST

# Step 1: Create a list of places to visit
places_to_visit = ["Manchester", "Paris", "Hawaii", "Beijing", "Cape Town"]

# Step 2: Print the original list (unsorted)
print("Original list:", places_to_visit)

# Step 3: Use sorted() to temporarily sort the list in alphabetical order (does not modify original list)
sorted_places = sorted(places_to_visit)

# Step 4: Print the temporarily sorted list
print("Temporarily sorted list (A-Z):", sorted_places)

# Step 5: Print the list sorted in reverse alphabetical order (temporary change)
print("Temporarily sorted list (Z-A):", sorted(places_to_visit, reverse=True))

# Step 6: Print the original list again to show it is unchanged
print("Original list after sorted() calls:", places_to_visit)

# Step 7: Reverse the order of the list (permanent change)
places_to_visit.reverse()
print("List after reverse():", places_to_visit)

# Step 8: Reverse the list again to restore original order
places_to_visit.reverse()
print("List after second reverse():", places_to_visit)

# Step 9: Permanently sort the list in alphabetical order
places_to_visit.sort()
print("List after sort() (A-Z, permanent):", places_to_visit)

# Step 10: Permanently sort the list in reverse alphabetical order
places_to_visit.sort(reverse=True)
print("List after sort(reverse=True) (Z-A, permanent):", places_to_visit)


# Exercise 3.9 DINNER GUESTS
# Using len() to print the number of guests invited
print(f"\nTotal number of guests invited: {len(guest_list)}")






