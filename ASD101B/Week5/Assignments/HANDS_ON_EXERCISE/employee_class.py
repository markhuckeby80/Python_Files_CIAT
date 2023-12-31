class Employee:

    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: " + self.__ID_number + \
               "\nDepartment: " + self.__department + \
               "\nJob Title: " + self.__job_title

# Create three instances of the Employee class
Emp1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
Emp2 = Employee("Mark Jones", "39119", "IT", "Programmer")
Emp3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

# Print the data
print(Emp1, '\n')
print(Emp2, '\n')
print(Emp3)
