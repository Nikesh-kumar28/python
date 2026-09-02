# How do you find the total number of elements inside a tuple?

# a = (14, 445, 4654, 7, 657, 65, 76578, 5, 876, 8, 768, 9, 89, 789, 67, 87, 68, 7, 68, 6, 768)
# print(len(a))

# How do you find how many times a specific value appears?
# a = (1, 2, 2, 2, 2, 3, 4, 5, 6, 2, 6, 7)
# print(a.count(2))
# print(a.count(3))

# How do you find the index of the first occurrence of an element?
# a = (1, 2, 2, 2, 2, 3, 4, 5, 6, 2, 6, 7)
# print(a.index(2))

# How do you unpack tuple elements into individual variables?
# a = (1, 2, 3)
# p, q, r = a
# print(p,q,r)

# a = (3, 4, 6)
# w, r, y = a
# print(w,r,y)

# How do you reverse a tuple using slicing?
# a = (2, 3, 4, 5, 7, 8, 9)
# print(a[:])
# print(a[::-1])

# How do you concatenate two tuples?
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# print(tuple1 + tuple2)

# How do you create a tuple that repeats elements 3 times?
# a = (1, 2, 3)
# print(a * 3)

# How do you extract a tuple containing only the first three elements?
# a = (1, 2, 3, 4, 5, 6, 7)
# print(a[:3])

# How do you check if an item exists in one line?
# a = (2, 4, 5, 7, 8, 9, 10, 11)
# print(7 in a)

# Can you change, add, or remove an element after creation? Explain why or why not.

# no because tuple is emutable so not allowed remove, add, in tuple


# With Loops


# Iterate through a tuple and print each element on a new line.
# a = ("how", "are", "you")
# for x in a:
#     print(x)

# Find the sum of all numerical elements using a for loop.
# a = (2, 3, 4, 6, 8, 90)
# add = 0
# for x in a:
#     print(x)
#     add = add + x
#     print(add)

# a = (2, 3, 4, 6, 8, 90, True, "hello", "hi", 34, 8)
# add = 0
# for x in a:
#     if type(x) == int:
#       add = add + x
#       print(x, add)
# print(add)


# Count how many even numbers a tuple contains using a loop.
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# counter = 0
# for x in a:

#     if x % 2 == 0:
#         counter = counter + 1
#         print(x , counter)

# a = (234, 56, 4567, 2345, 234, 23456, 3456, 2345678, 12345678)
# counter = 0

# for x in a:
#     if x % 2 == 0:
#         counter = counter + 1
#         print(x, counter)

# b = (1234, 123, 345, 4567, 234567, 123456789, 2345, 3456)
# counter = 0
# for x in b:
#     if x % 2 == 1:
#         counter = counter + 1
#         print(x, counter)

# Convert a tuple of strings into a single sentence using a loop.
# a = ("hello", "how", "you", "there")
# dummy_str = ""

# for x in a:
#     dummy_str = dummy_str +  x + " "
#     print(x, dummy_str)


# a = ("hello", "how", "you", "there")
# dummy_str = ''

# for x in a:
#     dummy_str = dummy_str + x + ' '
#     print(x, dummy_str)


# Check if an element exists without using the in keyword.
# a = (1, 2, 3, 4, 5, 6)

# for x in a:
#     if x == 3:
#         print("yes")

# a = (1, 2, 3, 4, 5, 6)

# for x in a:
#     if x == 6:
#         print("no")


# Create a new tuple containing only integers from a mixed tuple.
# a = (1, 2, 3, 4, 5, 6, 7, 8, "hello", "how", "there")
# int_list = []

# for x in a:
#     if type(x) == int:
#         int_list.append(x)

# print(tuple(int_list))


# a = ("hello", "how", "you", "there", 1, 2, 3, 4, 5, 6, 7, 8, 9)

# int_list = []

# for x in a:
#     if type(x) == int:
#         int_list.append(x)
# print(tuple(int_list))


# Find the largest number without using max().




# Copy tuple elements into a list in reverse order using a loop.
# Find the index of a specific element without using .index().
# Given a nested tuple, use nested loops to print every individual number.


