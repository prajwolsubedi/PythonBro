# Class methods = Allow operations related to the class
# Take (cls) as the first parameter, which represents the class itself.

#  Instance methods = Best for operations on instances of the class (objects)
#  Static methods = Best for utility functions that do not need access to class data
#  Class methods = Best for class-level data or require access to the class itself

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    #Class Method
    @classmethod
    def get_count(cls):
        return f"Total # of students : {cls.count}"

    @classmethod
    def get_total_gpa(cls):
        return f"Total gpa is : {cls.total_gpa}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"


student1 = Student("A", 3.2)
student2 = Student("B", 3.6)
student3 = Student("C", 4.0)
student4 = Student("D", 2.2)

print(Student.get_count())
print(Student.get_total_gpa())