# Class methods = Allow operations related to the class itself
#             Take(cls) as the first parameter, which represents the class itself.

class Student:
    count =0 

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_student_count(cls):
        return f"Total no. of students: {cls.count}"

student1 = Student("Anish", 3.42) 
student1 = Student("Arpu", 3.65)  


print(Student.count)