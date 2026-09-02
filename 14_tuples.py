# What is a Tuple?

# Think of a tuple as a fixed, unchangeable sequence of items. 
# If a list is a shopping list you can constantly update, 
# a tuple is more like a fixed set of coordinates (latitude, longitude) 
# or a record of a person's birth date that won't change.

#     Ordered: The items have a defined order, and that order is preserved.
#     Immutable: Once created, you cannot change, add, or remove items.
#     Heterogeneous: Tuples can contain items of different data types (integers, strings, floats, even other lists or objects).

# an empty tuple
# empty_tuple = ()
# print(empty_tuple)

# A tuple integers
# numbers = (1, 2, 3, 4, 5)
# print(numbers)
# print(type(numbers))

# a tuple of strings
# fruits = ("kajnd", "qkwjf", "ircbirhd", "oqwigbc", "awkucgb")
# print(f" tuple of fruits: {fruits}")

# A tuple of mixed data types
# mixed_tuple = ("hello", 1, 23, 3.14, False, (23, 456, ["sf"]))
# print(f" mixed_tuple: {mixed_tuple}")

# a tuple containing a list (nested mutable object)
# nested_tuple = (1, [2, 3], 4, "test")
# print( nested_tuple[1][0] )
# nested_tuple[1] = [2,3]
# nested_tuple[1][0] = 4
# nested_tuple[1][1] = 5
# nested_tuple[2] = 8
# print(nested_tuple)

# A tuple containing a list (nested mutable object)
# nested_tuple = (1, [2, 3], 4, "test")
# print(nested_tuple[1][0]) 
# nested_tuple[1][0] = 4
# nested_tuple[1][1]  = 56
# nested_tuple[2] = 9
# print(nested_tuple)

# Important: A single-element tuple requires a trailing comma!
# Without it, Python treats it as just the item itself, not a tuple.
# single_element_tuple = (5, )
# print(f"Single-element tuple: {single_element_tuple}, type: {type(single_element_tuple)}")

# test = (23)
# print(type(test))

# not_a_tuple = (3,)
# print(f" not_a_tuple: {not_a_tuple},type: {type(not_a_tuple)} ")

# creating a tuple without parentheses (tuple packing)
# packed_tuple = "a", 10, True
# print(packed_tuple)

# tuple unpacking

# a , b, c = 10, 20, 30
# print(a,b,c)

# a , b, c = 10, 20, 30, 40
# print(a,b,c)

# a , b, c = 10, 20
# print(a,b,c)

# my_tuple = (1, 2, 3, 4, 5)
# a, b, c, d, e = my_tuple
# print(a, b, c, d, e)


# # Accessing elements using positive indexing
# print(f"First element: {my_tuple[0]}")  
# print(f"Third element: {my_tuple[-2]}")  

# # Accessing elements using negative indexing
# print(f"Last element: {my_tuple[-1]}")   
# print(f"Second to last element: {my_tuple[-2]}") 

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(f"slice [2:6]: {numbers[2:6]}")

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# concatenated

# tuple1 = (1, 2)
# tuple2 = (3, 4)

# combined_tuple = tuple1 + tuple2
# print(f" concatenated tuple: {combined_tuple}")

# repetition

# tuple1 = (1, 2)
# tuple2 = (3, 4)

# repeted_tuple = tuple1 * 3
# print(f" repeted_tuple: {repeted_tuple}")

# tuple1 = (1, 2)
# tuple2 = (3, 4)
# print(tuple1 > tuple2)
# print(tuple1 < tuple2)
# print(tuple1 >= tuple2)
# print(tuple1 <= tuple2)

# membership

# tuple1 = (1, 2)
# tuple2 = (3, 4)
# print(5 in tuple1)
# print(1 in tuple1)
# print(5 not in tuple2)
# print(3 in tuple2)

# my_tuple = ("apple", "banana", "cherry")

# Attempting to change an element (will raise TypeError)
# my_tuple[1] = "grape"

# my_tuple_with_list = (1, [2, 3], 4)
# print(f"Original tuple with list: {my_tuple_with_list}") 

# my_tuple_with_list[1].append(5) # Modifying the list INSIDE the tuple
# print(f"Modified tuple with list: {my_tuple_with_list}") 
# This is allowed because you are not changing the tuple itself (i.e., you're not reassigning index 1 to a different object).
# You are changing the *contents* of the list object that index 1 points to.

# a = int(input("enter your number: "))
# b = int(input("enter your number: "))
# print(a,b)

# a = 2
# b = 5
# print(a, b)
# c = a

# a = b
# b = c
# print(a, b)
# a = b
# b = a
# print(a, b)

# a = 7
# b = 9
# print(a, b)

# d = a

# a = b
# b = d
# print(a, b)

# swapping variables easily using tuple unpacking

# a = 10
# b = 20
# a, b = b, a
# print(a, b)


# a, b = 20, 10 # Python first evaluates (b, a) as a tuple, then unpacks
# print(f"After swap: a={a}, b={b}") 

# Unpacking with * (star operator) for arbitrary remaining elements (Python 3+)
# coordinates = (1, 2, 3, 4, 5, 7, 8, 9, 10)
# a, b, c, d, *e = coordinates
# a, b, *c, d, e = coordinates
# a, *b, c, d, e = coordinates
# print(a, b, c, d, e)

# first, *middle, last = coordinates
# print(f"first={first}, middle={middle}, last={last}") 

# my_list = [1, 2, 3]
# my_tuple = tuple(my_list)
# print(my_tuple)

# my_list = [23, 456, 678, 789]
# my_tuple = tuple(my_list)
# print(my_tuple)

# my_list = (1, 2, 3, 56, 78)
# my_tuple = list(my_list)
# print(my_tuple)

# a = "this is a test class about tuples and it is a good example"
# b = a.split()
# ['this', 'is', 'a', 'test', 'class', 'about', 'tuples', 'and', 'it', 'is', 'a', 'good', 'example']
# c = tuple(b)
# ('this', 'is', 'a', 'test', 'class', 'about', 'tuples', 'and', 'it', 'is', 'a', 'good', 'example')
# print( c.count("is") )

# print(a.count("is"))

# type conversion
# a = [1, 2, 3, 4, 5]
# a = "jaipur"
# a = tuple(a)
# print(a)

