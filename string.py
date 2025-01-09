#Username validate excercise
# should not be more than 12
#should not contain any space
# should not contain any digits


# username = input("Enter username: ")

# if len(username)>12 or not username.isalpha():
#     print("Invalid user name")
# else:
#     print("Valid username")

# print(username.isalpha())
# print(len(username))


# Indexing - accessing  elements of a sequence using [] (indexing operator)
#  [start: end :step]

credit_card_number = "1234-5675-9874-5555"

print(credit_card_number[5])
print(credit_card_number[:5])
print(credit_card_number[5:])
print(credit_card_number[::3]) #count every third character from 0

#reverse string
print(credit_card_number[::-1])