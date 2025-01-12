# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex: phone, cup, book
# You need  a "class" to create  many objects

# class = (blueprint) used to design  the structure and layout of an object

class car:
    total_car =0
    def __init__(self, model, year, color,  for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        car.total_car = 1 # if we want to update variable of a class
    
    def getCarModal(self):
        return f"Your Car is {self.model}"

car1 = car("Thar", 2025, "black", True)

print(car1.getCarModal())

