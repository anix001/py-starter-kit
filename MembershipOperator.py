# Membership Operator = used to test a value  or variable is found in a sequence(string,list, set, tuple, dictionary)
# 1. in      2. not in



word = "apple"

letter = input("guess a letter in the secret word:")

if letter not in word:
    print("Oh, There is no such letter in word")


if letter in word:
    print(f"{letter} is in word")


email = "ani@gmail.com"

if '@' in email and '.' in email:
    print("valid email")
else:
    print("Invalid email")