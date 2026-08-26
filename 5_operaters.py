# arthmetic operators

# + add
# - sub
# * mul
# / divide
# % modules
# // flor division
# ** exponential

# print(10.2 + 5.8)

# print(10 - 2.0)

# print(10 - 2)

# print(10 / 2)

# print(10 // 2)

# print(10 ** 2)

# print("hello" + "world")

# print("4" * 10)

# a = "rewari,"
# b = "haryana"

# print(a + b)

# print(a * 3)

# print(3 * 67 + 87 / 6)

# Operator Precedence (BODMAS vs. PEMDAS)

# a = 9
# b = 12
# c = 3
# x = a - b / 3 + c * 2 - 1

# 9 - 12 / 3 + 3 * 2 - 1
# 9 - 4 + 3 * 2 - 1
# 9 - 4 + 6 - 1
# 15 - 5
 
# y = a - b / (3 + c) * (2 - 1)

# 9 - 12 / (3 + 3) * (2 - 1)
# 9 - 12 / 6 * 1
# 9 - 2 * 1
# 9 - 2

# z = a - (b / (3 + c) * 2) - 1

# 9 - (12 / ( 3 + 3 ) * 2) - 1
# 9 - (12 / 6 * 2) - 1
# 9 - 4 - 1
# 9 - 5 

# print("X = ", x)
# print("Y = ", y)
# print("Z = ", z)

# a = input("enter a number: ")
# a = int(a)
# b = input("enter a number: ")
# b = int(b)
# print(a + b)

# a = int(input("enter a number: "))

# b = int(input("enter a number: "))

# print(23 + 87.0)

# print(456 - 187)

# print(876 * 987)

# print(876 / 234)

# print(456 // 450)

# print(557 ** 987)

# find the 10% of a given number

# a = float(input("enter a number:" ))
# print(a * 19 / 100)

# a = 10
# b = 10
#  print(f"A={a} and B={b}, a+b = {a+b}")
#  print(f" A={a}and B={b}, a-b = {a-b} ")
#  print(f" A={a}and B={b}, a*b = {a*b} ")
#  print(f"A={a} and B={b}, a/b = {a/b}")
# print(f"A={a} and B={b}, a//b = {a//b}")
# print(f"A={a} and B={b}, a**b = {a**b}")
# print(f"A={a} and B={b}, a%b = {a%b}")

# Comparison Operators

# these are used to compare two values
# >  greater than a > b
# <  less than a < b
# ==  equal to  a == b
# >=  greater than or equal to a >= b
# <= less than or equal to  a <= b
# !=   not equal to   a != b


#  > greater then
#  print(5 > 10)

# < less then
#  print(50 < 10)

# == double =
# print(18 == 8)

# != not =
# print(18 != 18)

# >= greater then =
# print(188 >= 18)

# < less then =
#  print(1 <= 18)

# membership operators
# test membership in sequences like lists and strings:

# in true if present "a" in "cat"
# not in true if not present "x" not in "cat"

# a = "I live in india"
# print("I" not in a)


# amount = int(input("enter amount: "))
# intrest_rate = float(input("enter intrest rate: "))
# time = float(input("enter time in years like 2.5 or 5: "))

# intrest = (amount * intrest_rate * time) / 100

# print(f"you have to pay {intrest}/- in {time} years.")

# number = int(input("enter a number: "))
# print ( number > 50 and number < 100 )

# number = int(input("enter a number: "))
# print ( number > 60 and number < 100)

# number = int(input("enter a number: "))
# print( number > 35 or number < 100)

# number = int(input("enter a number: "))
# print (number > 95 or number < 111)

# number = int(input("enter a number: "))

# print( number % 3)

# number = int(input("enter a number: "))
# print( number % 3)

# number = int(input("enter a number: "))
# reminder = number % 3
# print(reminder == 0 )

# number = int(input("enter a number: "))
# print(number % 5)

# number = int(input("enter a number: "))
# reminder = number % 5
# print(reminder == 0)

# number = int(input("enter a number: "))
# print(number % 3 == 0 or number % 5 == 0)

# number = int(input("enter a number: "))
# print(number % 2 == 0 or number % 4 == 0)

# number = int(input("enter a number: "))
# print(number % 2 == 0 and number % 4 == 0)

# char = input("enter a character: ")
# print(char == "a" or char == "e" or char == "i" or char == "o" or char == "u")


### type conversion in boolen

# ""
# ()
# []
# {}
# 0
# False
# none 
# they all are false inke alawa kch bi aaye sab true fr valve "-ve" kyu na ho

####### and 
# -> if any value is false it will return the false one
# -> if both the values are true it will pick the right one 

# Left  |  Right   | Output
# True  | False     | False
# False  | True     | False
# False   | False    | False
# True   |  True     | True

######### OR
# -> if any value is true it will select that
# -> if all values are false it will select the right most


# Left    |  Right    | Output
# True    |  False    | True
# False   |  True     | True
# True    |  False    |  True
#  False  | False     | False 



# print( 32 and 56 and () and 87 )

# print(23 and [] and 34 and 45)

# print(23 or [] or 45 or 45)

# print({} or 23 or 45 or 78 )

# print("-" and 34 or 23 and 87 or 90 or 45 and 65 )

# print(" " and 0 or 23 and {} or 90 or () and 65 )

# print(True and True and "false" and True and 435)

# print(True and True and 0 and True and 435)

# print(True and True and [] and True and 435)

# print(34 and "-" or 67 and 34 or 786 or 456 and 768)
# (34 and "-") or (67 and 34) or 786 or (456 and 768)
# "-" or 34 or 786 or 768
# "-"

# char = input("enter a character: ")
# print(char =="A" or char == "E" or char == "I" or char == "O" or char == "U")


# char = input("enter a character: ")
# print(char =="A" or char == "E" or char == "I" or char == "O" or char == "U")


# a = input("enter your age: ")
# a = int(a)

# print(a > 18)


# a = input("enter your age: ")
# a = int(a)
# print(a < 20)

# a = input("enter a number: ")
# a = int(a)
# print(a > 0)

# a = input("enter a number: ")
# a = int(a)
# print(a > 6)

# a = int(input("enter your age: "))
# print(a < 54)

# print("a" < "A")

