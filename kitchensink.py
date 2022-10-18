# Variables can change type after being set
x = 1
x = "test"
print(x)

# Casting
print(str(2))  # '2'
print(int(2.1))  # 2
print(float(2))  # 2.0

# Get the type of a variable
print(type(1))
print(type("hello"))

# Single or dobule quotes make no difference - much like JavaScript

# naming convention
myvar = "John"
my_var = "John"
_my_var = "John"  # Gives a warning if it's not used, like a private field in C#
myVar = "John"
MYVAR = "John"  # This is interpreted as a constant but CAN be overwritten
myvar2 = "John"

# Naming of cariables with multiple words doesn't have a set style
# Be consistent
multiWordVar = 1
MultiWordVar = 1
multi_word_var = 1

# Variable assignments - can be done on one line but can look messy
a, b, c = 1, '2', 3
print(a)
print(b)
print(c)

# Unpacking tuples/arrays - similar to C#
my_array = [1, 2, 3]
one, two, three = my_array
print(one)
print(two)
print(three)

# Printing variables
hello, world = "hello", "world"
print(hello, world)  # separates with a space
print(hello + world)  # doesn't separate with space

# Variables must be cast to the same type if using concatenation
print("I am "+(str(32)+" years old"))
print("I am", 32, "years old")  # except when passed in as a parameter

# Variable scope

x = "this is global"


def something():
    x = "this is local"  # this x is local to the function
    print(x)


something()
print(x)  # x declared above is left alone


def setGlobalVar():
    # this will set a global variable that can be accessed by other functions
    global myGlobalVar
    myGlobalVar = "another global var"


setGlobalVar()
print(myGlobalVar)

globalVar2 = "change me"


def setGlobalVar2():
    global globalVar2
    globalVar2 = "I've changed the global var"


setGlobalVar2()
print(globalVar2)

multi_line_string = """Multiline 
string"""
print(multi_line_string)

# Strings are arrays of chars so a char can be retrieved by index
print(multi_line_string[6])

for char in multi_line_string:
    print(char)

# length
print(len(multi_line_string))

# True, "Multi" is in the variable, shorthand if-statement
print("Multi" in multi_line_string)
print("MMulti" not in multi_line_string)

# string ranges
print("1234567890"[2:5])  # index 2,3 and 4, not index 5
print("1234567890"[:5])  # everything up to but not index 5
print("1234567890"[5:])  # everything from index 5
# read this backwards, so index [2] from the end, to index [5] (not included) from the end
print("1234567890"[-5:-2])

# String functions
print("test".upper())
print("TEST".lower())
print("  test  ".strip())  # removes whitespace before and after
print("test".replace("t", "r"))
print("hello world".split(' '))

# Formatting strings
s = "This is a {} {}"
print(s.format("formatted", "string"))
# You can use indexes for formatting too
print('{0} {2} {1}'.format("eat", "shorts", "my"))

# Escaping characters
# https://www.w3schools.com/python/python_strings_escape.asp
# All string methods
# https://www.w3schools.com/python/python_strings_methods.asp

# Booleans
# The comparisons are the same as C#
print(1 == 1)
print(1 == 2)
print(1 <= 2)

# Any non-empty/0 value is true
print(bool(1))
print(bool("test"))
print(bool(["test", "something"]))

if (bool("test")):
    print("test is not null")

# Empty arrays, objects, strings and 0 is false
print(bool(0))
print(bool(""))
print(bool({}))
print(bool([]))
print(bool(None))

# iterating through list
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):  # range 0:3, so 0,1,2
    print(thislist[i])

# Can be shortened to this (think C# lambda function)
[print(x) for x in thislist]

# New lists can be created from an existing one
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Will contain items with the letter "a"
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Lists do not have to have the same data type in it
anylist = [1, "test", True]

# Lists can also be constrcted using the (()) syntax
thislist = list((1, 2, 3))

# For accessing elements, see line 109

# Checking if something is in the list
if "apple" in ["apple", "banana", "pear"]:
    print("yes, apple is in the list")

# Changing values
thislist = ["apple", "banana", "pear"]
thislist[1] = "orange"
print(thislist)

# Changing the range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  # replaces index 1 and 2
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# replaces index 1 and 2 with three items, extending the list
thislist[1:3] = ["blackcurrant", "watermelon", "grapes"]
print(thislist)
# Replaces index 1,2,3 with one item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant"]
print(thislist)

# Inserting items - inserts at index 1, pushes the rest after it
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # works the same as C# list.Insert(...)
print(thislist)

# Append to the end of the list
thislist.append("grapes")
print(thislist)

# Extend lists
list1 = [1, 2, 3]
list2 = ('3', '4', '5')
list3 = {"test": "hello"}
list1.extend(list2)  # This works with ANY list type
print(list1)
list1.extend(list3)  # This prints the KEYS, not the values
print(list1)
# Note, you cannot extend a dictionary to a list
# list3.extend(list2)
# print(list3)

# Remove items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # Removes by value
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # Remove the specified index and returns it
print(thislist)
thislist.pop()  # Removes from the end and returns it
print(thislist)
del thislist[0]  # Deletes specified index, does not return
print(thislist)
del thislist
# print(thislist) - This fails as the list does not exist
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# equivalent of C# loop through list by index
thislist = ["apple", "banana", "pear"]
for index in range(len(thislist)):
    print(thislist[index])

# Can also use a while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# List methods
# https://www.w3schools.com/python/python_lists_methods.asp


# Tuples
# These are declared in the same way as C#
# It's ordered and cannot change
mytuple = ("apple", "banana", "orange")
print(mytuple)
# Accessing by index is done in the same way as arrays/lists

# A tuple can have one item, but include a comma at the end, otherwise it's just a variable
thistuple = ("apple",)

# A tuple can also contain mixed types, same as a list

# Can use the constructor
thistuple = tuple((1, 2, 3))  # takes a tuple as the argument

# If you need to change values in a tuple, convert to list, change value, and then convert to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Unpacking tuples is done in the same way as C#
fruits = ("apple", "orange", "pear")
(apple, orange, pear) = fruits

# You can use an asterisk (*) if you want remaining values as a list
(apple, *other_fruits) = fruits
print(other_fruits)

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Joining tuples
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = t1 + t2
print(t3)

# Multiplying tuples (repeating them)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Sets
# Unchangeable, unordered, immutable, and duplicate items are ignored
thisset = {"apple", "banana", "cherry", "apple"}
# The order can be read differently every time
print(thisset)

# Dictionaries
# Accessed using a key
thisdict = {
    "model": "Mustang",
    "brand": "Ford",
    "year": 1964
}
print(thisdict["brand"])
# From Python 3.7  dictionaries do not change their order
# dictionary items can be of any type

# If-statements

if 1 > 2:
    print("1 > 2")
elif (2 < 1):
    print("2 < 1")
else:
    print("1 < 2")

# Ternary
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And / Or is used instead of || &&

# pass = this is the same as C# break keyword, but for an empty statement
if 2 > 1:
    pass

# While-loops
# Use an if-statement to run something once the while is False, if required
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For-loops
nums = [1, 2, 3]
for x in nums:
    print(x)

for x in nums:
    if x == 2:
        break  # Break can be used to break out of a loop
    print(x)

for x in nums:
    if x == 2:
        continue  # Continue can also be used
    print(x)

# Equivalent of
# for (var i = 0; i < 10, i+= 2)
for i in range(0, 10, 2):
    print(i)
else:
    # This won't be hit if there's a 'break' in the loop
    print('Loop has finished')


# Functions

# arbitrary args, same as params[] args in C#
def func_with_arbitrary_args(*args):
    print(args)


func_with_arbitrary_args(1, 2, "hello")


def my_named_func(arg3, arg2, arg1):
    print(arg1, arg2, arg3)


my_named_func(arg1="python", arg2="coding", arg3="rocks")

# dynamic args


def my_arbirary_function(**args):  # args are passed in as a dictionary
    print(args)


my_arbirary_function(fname="Omar", sname="Ebrahim")

# Lambda functions


def lambda_x(a, b): return a + b + 10


print(lambda_x(5, 1))
# It's the same as writing
# int Add(a b) => a + b + 10;

# Classes


class Person:
    def __init__(self, name, age: int) -> None:
        self.Name = str(name)
        self.Age = age

    def __str__(self) -> str:  # this is the same as a C# .ToString() override
        return "My name is "+self.Name+". I am "+str(self.Age)+" years old."


person = Person("Omar", 32)
print(person)

# inheritance


class Child(Person):
    def __init__(self, name, age: int, sport) -> None:
        super().__init__(name, age)
        self.Sport = sport

    def __str__(self) -> str:
        return super().__str__()+" I like playing "+self.Sport


child = Child("Dave", 15, "Rugby")
print(child)
