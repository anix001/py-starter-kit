# List Comprehension= A concise way to create list in python
#                     Compact and easier to read than traditional loops
#    expression for value in iterable  if condition]


doubles = [x*2 for x in range(1, 11)]


fruits =["apple", "mango"]
fruits_upper = [fruit.upper() for fruit in fruits]

numbers =[-1.2,3,4,5]

positive_numbers = [num for num in numbers if num <=0]