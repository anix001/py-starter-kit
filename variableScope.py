
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in (higher priority)

# Local : We can't access one variable on another variable

# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)


# func1()
# func2()


# Enclosed: one function into another

# def func1():
#     x = 1
#     def func2():
#         print(x)
#     func2()

# func1()


# Global: variable Outside the function

# x=3

# def func1():
#     x= 2
#     print(x)

# func1()


# Built-in

# from math import e

# def func1():
#     print(e)

# e = 3

# func1()

