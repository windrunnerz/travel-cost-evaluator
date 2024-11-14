# Membership Test in Python
# In Python, the "in" operator is used for membership testing.
# It checks if an element exists in a sequence or collection like lists, tuples, sets, strings, or dictionaries.

# Example with a list
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list of fruits.")

# Example with a string
sentence = "Hello, world!"
if "world" in sentence:
    print("The word 'world' is in the sentence.")

# Example with a dictionary (checks if key exists)
person = {"name": "Alice", "age": 25}
if "name" in person:
    print("The key 'name' is in the dictionary.")

# The "in" keyword returns True or False based on membership
# It can also be used with "not" to check if an element is not present
if "grape" not in fruits:
    print("Grape is not in the list of fruits.")
