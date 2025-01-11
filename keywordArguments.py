# Keyword Arguments = an argument preceded by identifier
# Advantage: Helps with readability
# Order of argument doesn't matter


def hello(name, message):
    print(f"Hey {name},  {message}")


# hello(message="I Really Miss you", name="Arpana")


# *args = allows  you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments

def sum(*args):
    total =0
    for arg in args:
        total += arg
    return total

print(sum(1,2,3,4,5))


def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="nzxnf", city="ktm", home="Manpur")