# number = [234 , 345, 12, 3456778, 198348, 10844, 984]
# print(number)
# print(number[-3])

# a = [234, 45.67, 'nikku', 9087, [23354]]
# print(a)
# print(a[4])

# a = [234, 45.67, 'nikku', 9087, [23354]]
# print(a)
# print(a[-1])

# a = [234, 45.67, 'nikku', 9087, [23354]]
# print(234, 45.67, 'nikku', 9087)

# a = [234.67, 3455, 'jacks', -23345, [234.76]]
# print(a)
# print(type(a[2]))

# a = [234.67, 3455, 'jacks', -23345, [234.76]]
# print(a)
# print(type(a[-2]))

# data = [234, True, 'nikesh', False, [1,2,3,4]]
# print(data)
# print(type(data[-1]))

# data = [234, True, 'nikesh', False, [1,2,3,4]]
# print(data)
# print(type(data[3]))

# data = [234, True, 'nikesh', False, [1,2,3,4]]
# print(data)
# print(type(data[2]))

# abc = [123, 456, 456, True, 23.456, ["nikesh", 123, [12345, [6787 ] ] ] ]
# print(abc[5])

# abc = [123, 456, 456, True, 23.456, ["nikesh", 123, [12345, [6787 ] ] ] ]
# print(abc[5][2])

# abc = [123, 456, 456, True, 23.456, ["nikesh", 123, [12345, [6787 ] ] ] ]
# print(abc[5][2][-1])

# abc = [123, 456, 456, True, 23.456, ["nikesh", 123, [12345, [6787 ] ] ] ]
# print(abc[5][2][-1][-1])

# abc = [7364, 73364, 948490, 1234, 98364, 923744, ["nnnn", 874, True,[234 [3984] ] ] ]
# print(abc[6][2][-1][-1])

# a = [ [ [ [ [ 123 ] ] ] ] ]
# print(a[0][0][0][0])

#### refrence variable

# a = 34
# b = a
# print(a,b)
# a = 23
# print(a,b)

# a = ['ghjk', 12234, 35475, 928475,92389]
# b = a
# print(a,b)
# b[0] = 'nikesh'
# print(a,b)


###### data manipulation

# a = [0,1, 2, 3, 4, 5, 6,]
# print(a[0])
# a[0] = 98
# print(a)

# b = [8734, 947, 98847, 947,947]
# print(b[4])
# b[4] = 1234556780997
# print(b)


##### identity opreator

# a = ['ghjk', 12234, 35475, 928475,92389]
# b =  ['ghjk', 12234, 35475, 928475,92389]
# print(a is b)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"slice[2:6]: {numbers[2:8]}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"slice[:5]: {numbers[:5]}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"slice[7:]: {numbers[7:]}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"slice[:]: {numbers[:]}")

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"slice[::4]: {numbers[::4]}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"reversedslice[::-1]: {numbers[::-1]}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"slice[::-3]: {numbers[::-3]}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(f"slice[1:8:2]: {numbers[-8:-1:2]}")

# numbers = [123, 345, 456, 678, 789, 879, 987]
# print(numbers[-3:-8:-2])

# my_list = ["apple", "banana", "cheery", "date"]
# print(my_list[1][2:4])

# my_list = ["apple", "banana", "cheery", "date"]
# print(my_list[2][-3:-1])

# my_list = ["apple", "banana", "cheery", "date"]
# print(my_list[3][-4:-2:-1])

# a = ["india", "france", "usa", "japan"]
# print(a[0][0])
# print(a[0][2])
# print(a[-1][-1])

# a = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70,80,90]
# ]
# print(a[0])
# print(a[2])
# print(a[2][0])
# print(a[1][2])

# students = [
#     ["rahul", 20],
#     ["priya", 21],
#     ["amit", 19]
# ]
# print(students[0][0])
# print(students[-1])
# print(students[-1][-1])

# data = [
#     100,
#     "python",
#     [10, 20, 30],
#     True,
#     ["india", "japan", "usa"]
# ]
# print(data[1])
# print(data[2][0])
# print(data[4][-1])
# print(data[2][-1])

# a = [
#     "hello",
#     [1, 2, 3],
#     "india",
#     [True, False, [100, 200, 300]]
# ]
# print(a[0][1])
# print(a[1][2])
# print(a[3][2][1])

# log_entry = "[error]===system clash==="
# print(log_entry.rstrip("="))

# document = "final_report.pdf"
# print(document.endswith(".pdf"))

# my_list = ["apple", "banana", "cheery", "date"]
# print(my_list[1][2:4])
# my_list[1] = "grape"
# print(f" modified single element: {my_list}")

# my_list = ["apple", "banana", "cheery", "date"]
# my_list[2] = "grape", "gavava"
# print(f"{my_list}")

# my_list = ["apple", "banana", "cheery", "date"]
# my_list[0:2] = ['mango', 'blueberry']
# print(f" {my_list}")

# my_list = ["gavava", "orange", "onion", "mango"]
# my_list[1:2] = ['papaya', 'dragonfruit']
# print(f" {my_list}")

# my_list = ["apple", "banana", "cheery", "date"]
# my_list[2:4] = ["mango", 'orange', 'gavava']
# print(f" {my_list}")

# list1 = [8, 90, 'yrt']
# list2 = [23, 678, 'vfx']
# combinedlist = [list1 + list2]
# print(f" {combinedlist}")

# list1 = [98, 89, 'iuy']
# list2 = [89, 65, 'imj']
# repeted_list = list1 * 4
# print(f" {repeted_list}")

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(a[::-1])
# print(a[::-2])
# print(a[-5:])
# print(a[:-5])
# print(a[-8:-3])
# print(a[-3:-8:-1])
# print(a[-2:-10:-2])


# ll = ["qwer", 'wjhef', 'kfnfekj', [23, 789, 8907], 'jnjr']
# ll.append('nikku')
# print(ll)

# pop = ['afbhb', 'jbhf', 'iqhdf', 'kqwdb', [234, 4456, 678, 678], 'xgh']
# pop.append('bullshit')
# print(pop)

# listw = ['banana', 'apple', 'gavava', 'cheery', 123, [1,2]]
# listw.insert(3, 'grape')
# print(listw)

# loik = ['asus', 'lenovo', 'victus', 'hp', 'dell', 'mackbook', [123, 446], 12, 3,4]
# loik.insert(6, 'oppo')
# print(f" {loik}")

# loik = ['asus', 'lenovo', 'victus', 'hp', 'dell', 'mackbook', [123, 446], 12, 3,4]
# loik.insert(-4, 'lava')
# print(f"after insert: {loik}")

# loik = ['asus', 'lenovo', 'victus', 'hp', 'dell', 'mackbook', [123, 446], 12, 3,4]
# loik.insert(90, 'realme')
# print(loik)

# loik = ['asus', 'lenovo', 'victus', 'hp', 'dell', 'mackbook', [123, 446], 12, 3,4]
# loik.insert(-21, 'vivo')
# print(loik)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.append([1, 2, 3, 4])
# print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# a.extend([1, 2, 3, 4])
# print(a)

# b = [45, 67,89, 90, 23, 43, 93487, 9987, 87 ]
# b.append([1,2,3,4])
# print(b)
# b.extend([1,3,4,5,6])
# print(b)

# v = ['sjgf', 'jsfh', [1, 3, 5, 6, 7], 'mzjgf', 'kfh', [12, 34, 56, 78]]
# v.extend([00,00,00])
# print(v)

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b.append('hello')
# b.extend('hello')
# print(b)

# my_list = ['apple', 'cheery', 'banana', 'apple', 123, [1,2]]
# my_list.remove('apple')
# print(my_list)

# my_list = ['apple', 'cheery', 'banana', 'apple', 123, [1,2]]
# my_list[0] = 'vivo'
# print(my_list)

# my_list = ['apple', 'cheery', 'banana', 'apple', 123, [1,2] ]
# my_list[5] = 'realme'
# print(my_list)

# my_list = ['apple', 'cheery', 'banana', 'apple', 123, [1,2]]
# del my_list[-3]
# print(my_list)

# a = 23
# del a
# print(a)

# my_list = ['apple', 'cheery', 'banana', 'apple', 123, [1,2]]
# my_list.pop(-4)
# print(my_list)

# my_list = ['apple', 'cheery', 'banana', 'apple', 123, [1,2]]
# print(my_list.pop())
# print(my_list)

# my_list = ['apple', 'cheery', 'banana', 'apple', 123, [1,2]]
# print(my_list.pop())
# print(my_list)

# number = [4, 6, 8, 1, 0, 45, 44, 67]
# number.sort()
# print(number)

# number = [4, 6, 8, 1, 0, 45, 44, 67]
# number.sort(reverse = True)
# print(number)

# word = ['apple', 'cheery', 'nikku', 'sonm', 'viraj', 'mohs', 'bsert']
# word.sort()
# print(word)

# word = ['apple', 'cheery', 'nikku', 'sonm', 'viraj', 'mohs', 'bsert']
# word.sort(reverse = True)
# print(word)

# sorted_list = sorted([1, 2, 4, 3, 5, 6, 4, 3, 2, 1])
# print(sorted_list)

# sorted_list = sorted([1, 2, 4, 3, 5, 6, 4, 3, 2, 1], reverse = True)
# print(sorted_list)

# list = [1, 2, 2, 2, 3, 4, 5, 6, 2, 7, 2]
# print(f" count of 2: {list.count(2)}")

# list = [1, 2, 2, 2, 3, 4, 5, 6, 2, 7, 2]
# print(f" count of 3: {list.count(3)}")

# list = [1, 2, 2, 2, 3, 4, 5, 6, 2, 7, 2]
# print(f" count of 10: {list.count(10)}")

# oer = ['orange', 'apple', 'gavava', 'strawberry', 'dragonfruit']
# print(oer.index('gavava'))

# my_list = [1, 23, 334, 34]
# my_list.reverse()
# print(my_list)

# a = [1, 2, 3]
# b = a
# print(a,b)
# b.pop()
# print(a,b)

# a = [23, 45, 67, 78, 89, 77, 67]
# b = a.copy()
# b.append(89)
# print(a)
# print(b)

# a = [23, 45, 67, 78, 89, 77, 67]
# a.clear()
# print(a)

# a = ['hello', 'how', 'are', 'you']
# b = len(a)
# print(b)

# a = ['hello', 'how', 'are', 'you']
# for x in a:
#     print(x)

# a = ['hello', 'how', 'are', 'you']
# for x in a:
#     for y in x:
#         print(y)

# a = 'this is a test py and small'
# b = a.split()
# print(type(b))
# print(a)
# print(b)

# a = '''
#     hello this is a split sctreen
#     of
#     multiple methofs
#     lines'''
# print(a.split())
# print(a)

# a = "2/2/2005"
# print(a.split())
# print(a)

# a = "2/2/2005"
# print(a.split('/'))
# print(a)

# a = "28-04-2005"
# print(a.split("-"))
# print(a)

# a = "apple","bamnaan","leomon"
# print(a.split())
# print(a)

# words = ['i', 'love', 'python']
# print("-".join(words))
# print(words)

# a = ['jsgv', 'jfhewhr', 'jewrh', 'kefh']
# print("/".join(a))

# words = ["hello", "word", "python"]
# ", ".join(words)
# print(words)

# Try to predict the output before running the code.

# fruits = ["apple", "banana", "mango", "orange"]

# print(fruits[0]) 
# print(fruits[2]) 
# print(fruits[-1])

# numbers = [100, 200, 300, 400, 500]

# print(numbers[1])
# print(numbers[-2]) 
# print(numbers[4])

# current_actions = ["line", "circle", "square"]
# backup_actions = current_actions
# current_actions.append("triangle")

# print(current_actions)
# print(backup_actions)

# cart = ["shoes", "shirt", "watch", "hat", "belt", "socks"], 
# # write a single line using negative list slicing to extract exactly the last 3 items.

# print(cart[-3:])

# a = ["hello", "how", "are", "you"]

# i = 0
# while i < len(a):
#     print(a[i])
#     i+= 1

# new_list = []
# i = 1
# while i <= 10:
#     number = int(input("enter your number: "))
#     new_list.append(number)
    
#     i += 1
# print(new_list)


# i = 1
# while i <= 10:
#     new_list = []
#     number = int(input("enter your number: "))
#     new_list.append(number)
#     print(new_list)
#     i += 1

# new_list = []
# for x in range(10):
#     number = int(input("enter your number: "))
#     new_list.append(number)
#     print(new_list)

# new_list = []
# for x in range(10):
#     number = int(input("enter your number: "))
#     new_list.insert(0, number)
#     print(new_list)

# Print each element on a new line using a for loop.

# my_list = [10, 34, 56, 67, 68, 67]
# for element in my_list:
#     print(element)

# new_list = [234, 56, 67, 567, 67, 567, 567]
# for element in new_list:
#     print(new_list)

# Find the sum of all numerical elements using a loop.
# add = 0
# a = [1, 2, 3, 4, 5, 6, 7]

# for x in a:
#     add = add + x
#     print(add)

# add = 0
# a = [23, 34, 567, 67, 67, 789, 6789, 789,]
# for x in a:
#     add = add + x
#     print(add)

# a = [1, 2, 3, 4, 5, 6, 7, "hello", "how", "are", "you"]
# add = 1

# for x in a:
#     if type(x) == int:
#         add = add * x
#         print(add)

# a = [12, 34, 456, 'asd', 'qwd', 'qwerf']
# add = 0

# for x in a:
#     if type(x) == int:
#         add = add + x
#         print(add)

# Find the largest number without using max().

# a = [12, 34, 456, 345, 56, 56, 12345, 123456]
# largest = a[0]

# i = 1
# while i < len(a):
#     if a[i] > largest:
#       largest = a[i]
#     i += 1
# print(largest)

# a = [23, 45, 567, 789, 56890]
# largest = a[0]

# i = 1
# while i < len(a):
#     if a[i] > largest:
#         largest = a[i]
#     i+= 1
# print(largest)

# a = [23, 23, 34, 456, 567, 23, 45]
# largest = a[0]

# for x in range(1 , len(a)):
#     if a[x] > largest:
#         largest = a[x]
#     print(f" largest: {largest} ")

# a = [1, 2, 3, 4, 5, 8, 5, 9, 7, 10, 2]
# largest = a[0]

# for x in range(1, len(a)):
#     if a[x] > largest:
#         largest = a[x]
#     print(f" largest: {largest}")

# Count how many times a specific element appears using a loop.

# counter = 0
# a = [1, 2, 2, 2, 3, 4, 5, 6, 7]

# for x in a:
#     if x == 2:
#         counter += 1
# print(counter)

# Create a new list containing squares of all numbers from an existing list

# a = [1, 2, 2, 2, 3, 4, 5, 6, 7]
# new_list = []

# for x in a:
#     new_list.append(x * x)
#     print(new_list)


# b = [1, 2, 3, 5, 7, 8, 9]
# new_list = []

# for x in b:
#     new_list.append(x * x)
# print(new_list)

