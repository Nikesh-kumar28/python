###### operators

# print(10 / 2)

# print(100 / 2)

# print(1000 // 2)

# print(10 ** 2)

# print(10 * 2)

# print("hello" + "world")

# print("4" * 10)

# print("23" * 6)

# a = "rewari"
# b = "haryana"
# print(a + b)

# print(3 * 67 + 87 / 6)

# a = 7
# b = 9
# c = 5
# x = a - b / 3 + c * 2 - 1
# x = 7 - 9 / 3 + 5 * 2 - 1
# x = 7 - 3 + 5 * 2 - 1
# x = 7 - 3 + 10 - 1
# x = 17 - 4
# print(a)

#  y = a - b / (3 + c) * (2 - 1)

# a = input("enter a number: ")
# a = int(a)
# b = input("enter a number: ")
# b = int(b)
# print(a + b)

# a = float(input("enter a number:" ))
# print(a * 19 / 100)

# a = 10 
# b = 10

# print(f"A = {a} and B = {b}, a+b = {a + b}")
# print(f"A = {a} and B = {b}, a-b = {a - b}")
# print(f"A = {a} and B = {b}, a*b = {a * b}")
# print(f"A = {a} and B = {b}, a/b = {a / b}")
# print(f"A = {a} and B = {b}, a//b = {a // b}")
# print(f"A = {a} and B = {b}, a**b = {a ** b}")
# print(f"A = {a} and B = {b}, a%b = {a % b}")


# print(50 > 49)

# print(90 > 89)

# print(98 < 97)

# print(87 < 85)

# print(88 == 88)

# print(90 == 90)

# print(90 != 90)

# print(90 >= 90)

# print(56 <= 55)

# a = "i live in india"
# print("i" not in a)

# a = 'i live in india'
# print("live" in a)


# amount = int(input("enter amount: "))
# intrest_rate = float(input("enter intrest rate: "))
# time = float(input("enter time in years like 2.5 or 5: "))


# number = int(input("enter a number: "))
# print ( number > 50 and number < 100 )

# number = int(input("enter a number: "))
# print(number > 49 and number < 100)


# number = int(input("enter a number: "))
# print( number % 3)

# number = int(input("enter a number: "))
# print(number % 2)


# number = int(input("enter a number: "))
# reminder = number % 3 
# print(reminder == 0)

# char = input("enter a character: ")
# print(char =="A" or char == "E" or char == "I" or char == "O" or char == "U")

# a = int(input("enter your age: "))
# print(a < 20)



# if else 

# number = -4 
# if number > 0:
#     print("it's" +ve)
# else:
#     print("-ve")

# number = -4 
# if number < 0:
#     print("it +ve")
# else:
#     print("-ve")

# age = 15

# if age >= 20:
#     print("you caan vote")

# else:
#     print("you can't vote")

# score = int(input("enter your score: "))

# if score > 33:
#     print ("you pass in exam")
# else:
#     print("you fail in exam")

# a = "i"

# if a == "a":
#     print("yes")
# elif a == "e":
#     print("yes")
# elif a == "i":
#     print("yes")
# elif a == "o":
#     print("yes")
# elif a == "u":
#     print("yes")
# else:
#     print("no")

# a = int(input("enter your number: "))

# if a == 1:
#     print("monday")

# elif a == 2:
#     print("tuesday")

# elif a == 3:
#     print("wednesday")

# elif a == 4:
#     print("thursday")

# elif a == 5:
#     print("friday")

# elif a == 6:
#     print("saturday")

# elif a == 7:
#     print("sunday")

# else:
#     print("invalid")

# a = 'hello'
# i = 0
# vow = 0
# while i < len(a):
#     if a[i] in 'aeiou':
#         vow += 1
#     i += 1
# print(vow)



### with loops

# Write a program to find and print the total number of spaces inside a string.

# a = "i live in india."

# count = 0
# for x in a:
#     if x == " ": 
#       count += 1
# print(count)

# a = "i live in india."

# count = 0
# i = 0

# while i < len(a):

#     if a[i] == " ":
#         count += 1
    
#     i += 1
# print(count)

# Write a program to count the total number of vowels in a string using a loop.


# a = "a e i o u "
# count = 0

# for x in a:
#     if x == " ":
#         count += 1
# print(count)

# a = "a e i o u "

# count = 0
# i = 0

# while i < len(a):
#     if a[i] == " ":
#         count += 1
#     i += 1
# print(count)  

# Write a program to reverse a given string using a for loop.

# a = 'indiapython'
# reverse = ""

# for x in a:
#     reverse = x + reverse

# print(reverse)


### intermidiate

# Write a program to check whether a given string is a palindrome using loops

# a = "nitin"
# # print(a[::-1])

# if a == a:
#     print('palindrome')
#     print('True')
# else:
#     print('not palindrome')

# Write a program that converts every alternate character to uppercase (e.g., "python" → "PyThOn").

# data = 'python'
# for x in range(len(data)):
#     if x % 2 == 0:
#         print(data[x].upper())
#     else:
#         print(data[x])

# write a program to extract and print only the numerical digit from a mixed string

# a = "this is day 20 of my class and we try indexing from numbers 1, 2, 3, 4 and so on."

# for x in a:
#     if x in "0123456789":
#         print(x)

# v = "s,,j,hf 5637 74283 sjhyf 867"

# for x in v:
#     if x in "0123456789":
#       print(x)

# a = "this is day 20 of my class and we try indexing from numbers 1, 2, 3, 4 and so on."

# for x in a:
#     if x not in "0123456789":
#         continue
#     print(x)

# Write a program to remove all duplicate characters from a string using loops.

# a = "this is the very beautiful flower"

# for x in a:
#     if a.count(x) == 1:
#         print(x)

# a = "this is the very beautiful flower"

# for x in a:
#     if a.count(x) == 2:
#         print(x)

# i = 1
# total = 0

# while i <= 10:

#     item = int(input("enter your item price: "))
#     if item > 0:
#         total =+ item
#         i += 1

# Write a program to count how many times a specific character appears without using .count().

# text = "banana"
# char = 'a'

# count = 0

# for ch in text:
#     if ch == char:
#         count += 1
# print(count)

# text = "apple"
# char = "p"

# count = 0

# for ch in text:
#     if ch == char:
#         count += 1
# print(count)

