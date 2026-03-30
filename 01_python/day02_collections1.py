print("Day 2 - Collections I")

# Question 1: String indexing and slicing
# Create a string variable called word.
# Use any word you want.
# Then print:
# - the whole word
# - the first character
# - the last character
# - the first 4 characters

word = "python"

print(word)
print(word[0])
print(word[-1])
print(word[:4])


# Question 2: List basics
# Create a list with 5 items.
# Then print:
# - the whole list
# - the first item
# - the last item
# - items 2 to 4 using slicing

fruits = ["Apple", "Banana", "Orange", "Pineapple", "Mango"]

print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:4])


# Question 3: Change and add to a list
# Using the list from Question 2:
# - replace one item
# - add one new item using append()
# - print the updated list

fruits[0] = "Aranciata"
fruits.append("Honey")
print(fruits)


# Question 4: Remove from a list
# Using the same list:
# - remove one item using remove()
# - remove one item using pop()
# - print the popped item
# - print the final version of the list

fruits.remove("Aranciata")
popped_item = fruits.pop()

print(popped_item)
print(fruits)


# Question 5: Tuple vs list
# Create:
# - one tuple with 3 items
# - one list with 3 items
#
# Then:
# - print both
# - change one item in the list
# - print the changed list
# - print the tuple unchanged

cities_tuple = ("London", "Paris", "Nairobi")
cities_list = ["London", "Paris", "Nairobi"]

print(cities_tuple)
print(cities_list)

cities_list[1] = "Lagos"

print(cities_list)
print(cities_tuple)
