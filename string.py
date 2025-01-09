#Username validate excercise
# should not be more than 12
#should not contain any space
# should not contain any digits


username = input("Enter username: ")

if len(username)>12 or not username.isalpha():
    print("Invalid user name")
else:
    print("Valid username")

# print(username.isalpha())
# print(len(username))b