# if __name__  == __main__: (this script can be imported OR run standalone)
#                          Functions and classes in this module can be reused
#                          without the main block of code executing

# ex. library = import library for functionality
#               when running library directly, display a help page

# def main():
    # your program code goes here

# if __name__ == '__main__':
#     main()

print(__name__)

# The “if __ name __ == '__ main __'” statement in Python checks if the current script is being run directly as the main program, or if it's being imported as a module into another program. __name__ is a variable that exists in every Python module, and is set to the name of the module.