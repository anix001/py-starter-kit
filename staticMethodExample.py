# Static Method= A method that belongs to a class rather than any object from that class (instance)
# Usually used for general utility functions

# Instance method = Best for operations on instance of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    #Instance Method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod # we do not need objects data for this method
    def is_valid_position(position):
        valid_positions = ["Manager", "cook", "Cashier"]
        return position in valid_positions


print(Employee.is_valid_position("cook")) # We donot need to create obj to execute this method