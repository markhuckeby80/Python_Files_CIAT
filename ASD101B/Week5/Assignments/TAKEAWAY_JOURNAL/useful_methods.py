class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Accessor Method
    def get_age(self):
        print("Fetching age data...")
        return self.age


# Create a new Student object
student = Student("Mark", 43)

# Using Accessor Method
age = student.get_age()
print("Student's age:", age)
