# Python file detection

import os

file_path = "test.txt"

# if os.path.exists(file_path):
#     print("Yeah it exists")

#     if os.path.isfile(file_path):
#         print("That is  a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")

# Python writing files(.txt, .json, .csv)


# txt_data="I like pizza!!"

file_path = "output.txt"

# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")


# read file
with open(file_path, "r") as file:
    content = file.read()
    print(content)
