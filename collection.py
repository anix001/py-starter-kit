# Collection - a single "variable" used to store multiple values
#  List = [] ordered and changeable, duplicates ok
# Set = {} unordered and immutable , but add/remove okay, no duplicates 
# Tuple = () ordered and unchangable, duplicates, Faster

fruits = ["aa", "bb", "cc", "dd"]

# print(fruits[::-1])

print("aa" in fruits) # true just like includes in js


for fruit in fruits:
    print(fruit, end=" ")
